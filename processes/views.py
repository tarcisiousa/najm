import os
from datetime import date

from django.conf import settings
from django.contrib import messages
from django.db.models import ProtectedError, Count
from django.http import HttpResponseRedirect, FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from agendas.models import AgendaModel
from assisteds.forms import AssistedsDocumentForm
from assisteds.models import AssistedDocumentModel, AssistedsModel
from responsibles.forms import ResponsiblesDocumentsForm
from responsibles.models import ResponsiblesDocumentsModel
from . import metrics
from .models import ProcessesModel, ProcessDocumentModel, ProcessesNotesModel
from .forms import ProcessesForm, ProcessesDocumentForm, ProcessesNotesForm
from requireds.forms import RequiredsForm


class ProcessesList(ListView):
    model = ProcessesModel
    template_name = 'processes_list.html'
    context_object_name = 'processes'

    def get_queryset(self):
        processes = ProcessesModel.objects.all()
        search_protocol = self.request.GET.get('search-process', '')
        search_today = self.request.GET.get('today', '')
        search_pending = self.request.GET.get('search_pending', '')
        search_phase = self.request.GET.get('search_phase', '')

        if search_protocol:
            processes = processes.filter(protocol__icontains=search_protocol)

        if search_today:
            today = date.today()
            processes = processes.filter(date_at__icontains=today)

        if search_pending:
            processes_notes = []
            for item in processes:
                if item.notes > 0:
                    processes_notes.append(item)
            processes = processes_notes

        if search_phase:
            status_phase = self.request.GET.get('status_phase', '')
            processes = processes.filter(phase=status_phase)

        return processes

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        processes = ProcessesModel.objects.all()
        notes = ProcessesNotesModel.objects.all()
        notes_info_list = []
        for process in processes:
            for note in notes:
                if process.pk == note.id_process.id:
                    if note.status == '0':
                        if process.pk in notes_info_list:
                            pass
                        else:
                            notes_info_list.append(process.pk)
        print(notes_info_list)
        context['notes_info_list'] = notes_info_list
        return context

class ProcessesCreate(CreateView):
    model = ProcessesModel
    form_class = ProcessesForm
    template_name = 'processes_create.html'
    success_url = '/processes/list/'
    
    def form_valid(self, form):
        self.object = form.save()  # Salva e atribui o objeto a self.object
        today = date.today()
        protocol = f'{today}{self.object.pk}'.replace('-','')  # Agora usa self.object.pk
        self.object.protocol = protocol
        self.object.date_at = today
        return super().form_valid(form)


class ProcessesDetail(DetailView):
    model = ProcessesModel
    template_name = 'processes_detail.html'


class ProcessesUpdate(UpdateView):
    model = ProcessesModel
    form_class = ProcessesForm
    template_name = 'processes_update.html'
    success_url = '/processes/list/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        request = self.request
        context = metrics.get_context_data(request, instance, context)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_notes = ProcessesNotesForm(request.POST)
        id_assisted = self.request.POST.get('add_required','')
        save_process = self.request.POST.get('save_process','')
        date_at = self.request.POST.get('date_at', '')
        categorie = self.request.POST.get('category', '')
        sub_categorie = self.request.POST.get('subcategory', '')
        sub_categorie_2 = self.request.POST.get('subcategory2','')
        add_note = self.request.POST.get('add_note', '')
        note_id = self.request.POST.get('note_id', '')
        id_process = self.request.POST.get('id_process', '')

        if id_assisted:
            requireds_form = RequiredsForm(request.POST)  # O form de Requireds
            requireds_form.instance.id_assisted = self.object.id_assisted

            if requireds_form.is_valid():
                required_instance = requireds_form.save()  # Salvar o formulário e salvar a instância
                processes = ProcessesModel.objects.filter(pk=self.object.pk).first() #atualizando processo
                processes.id_required = required_instance
                processes.save()
                return HttpResponseRedirect(reverse('processes_update', kwargs={'pk': self.object.pk}))
            else:
                print(requireds_form.errors)  # Exibir erros, caso existam
                return self.render_to_response({'requireds_form': requireds_form})

        if save_process:
            form = self.get_form()
            agenda_protocol = AgendaModel.objects.filter(protocol=self.object.protocol)
            if form.is_valid():
                self.object.date_at = date_at
                self.object.processes_matter = categorie
                self.object.processes_classs = sub_categorie
                self.object.processes_subject = sub_categorie_2

                if len(agenda_protocol) > 1: # Se houver mais de um agendamento
                    for agenda_exist in agenda_protocol:
                        agenda_exist.status = '1'
                        agenda_exist.save()
                else: #Se for o primeiro agendamento
                    agenda_protocol = AgendaModel.objects.filter(protocol=self.object.protocol).first()
                    agenda_protocol.status = '1'
                    agenda_protocol.save()
                print('deu certo')
                return self.form_valid(form)
            else:
                print(form.errors)
                return self.form_invalid(form)

        if add_note:
            if form_notes.is_valid:
                form_notes.id_process = id_process
                form_notes.save()

                process_current = ProcessesModel.objects.filter(pk=self.object.pk).first()
                process_current.notes += 1
                process_current.save()


                return HttpResponseRedirect(reverse('processes_update', kwargs={'pk': self.object.pk}))
            else:
                print(form_notes.errors)
                return HttpResponseRedirect(reverse('processes_update', kwargs={'pk': self.object.pk}))

        if note_id:
            note_current = ProcessesNotesModel.objects.filter(pk=note_id).first()
            note_current.status = '1'
            note_current.save()

            process_current = ProcessesModel.objects.filter(pk=self.object.pk).first()
            process_current.notes -= 1
            process_current.save()
            return HttpResponseRedirect(reverse('processes_update', kwargs={'pk': self.object.pk}))
class ProcessesUpdateDocumentProcess(UpdateView):
    template_name = 'processes_update_documents_process.html'
    model = ProcessesModel
    form_class = ProcessesDocumentForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        instance = self.get_object()
        documents_process = ProcessDocumentModel.objects.filter(id_process=instance.pk)
        if self.request.POST:
            context['form_process'] = ProcessesDocumentForm(self.request.POST)
        else:
            context['form_process'] = ProcessesDocumentForm(initial={'id_process': instance.pk})

        context['documents_process'] = documents_process
        return context

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        form_process = ProcessesDocumentForm(request.POST, request.FILES)
        id_document = self.request.POST.get('delete-document','')
        id_process = self.request.POST.get('id_process', '')

        if id_document:
            document = ProcessDocumentModel.objects.filter(pk=id_document).first()
            if document and document.file:
                file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))

                # Verifica se o arquivo realmente existe no sistema de arquivos e o remove
                if os.path.exists(file_path):
                    os.remove(file_path)
            document.delete()
            return HttpResponseRedirect(reverse('processes_update_documents_process', kwargs={'pk': instance.pk}))

        if id_process:
            if form_process.is_valid():
                form_process.save()
                return HttpResponseRedirect(reverse('processes_update_documents_process', kwargs={'pk': instance.pk}))
            else:
                print(f'Esses são os erros = {form_process.errors}')
                return HttpResponseRedirect(reverse('processes_update_documents_process', kwargs={'pk': instance.pk}))

class ProcessesUpdateDocument(UpdateView):
    template_name = 'processes_update_document.html'
    model = ProcessesModel
    form_class = ProcessesForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        instance = self.get_object()
        documents_assisted = AssistedDocumentModel.objects.filter(id_assisted=instance.id_assisted)
        documents_responsible = ResponsiblesDocumentsModel.objects.filter(id_responsible=instance.id_responsible)
        if self.request.POST:
            context['form_assisted'] = AssistedsDocumentForm(self.request.POST)
            context['form_responsible'] = ResponsiblesDocumentsForm(self.request.POST)
        else:
            context['form_assisted'] = AssistedsDocumentForm(initial={'id_assisted': instance.id_assisted})
            context['form_responsible'] = ResponsiblesDocumentsForm(initial={'id_responsible': instance.id_responsible})

        context['documents_assisted'] = documents_assisted
        context['documents_responsible'] = documents_responsible
        return context

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        form_assisted = AssistedsDocumentForm(request.POST, request.FILES)
        form_responsible = ResponsiblesDocumentsForm(request.POST, request.FILES)
        id_document_assisted = self.request.POST.get('delete-document','')
        id_document_responsibles = self.request.POST.get('delete-document-responsibles', '')
        id_assisted = self.request.POST.get('id_assisted', '')
        id_responsible = self.request.POST.get('id_responsible', '')

        print(f'ID - {id_responsible}')

        if id_document_assisted:
            document = AssistedDocumentModel.objects.filter(pk=id_document_assisted).first()

            if document and document.file:
                file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))

                # Verifica se o arquivo realmente existe no sistema de arquivos e o remove
                if os.path.exists(file_path):
                    os.remove(file_path)

            document.delete()
            return HttpResponseRedirect(reverse('processes_update_documents', kwargs={'pk': instance.pk}))

        if id_document_responsibles:
            document = ResponsiblesDocumentsModel.objects.filter(pk=id_document_responsibles).first()
            if document and document.file:
                file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))
                # Verifica se o arquivo realmente existe no sistema de arquivos e o remove
                if os.path.exists(file_path):
                    os.remove(file_path)
            document.delete()
            return HttpResponseRedirect(reverse('processes_update_documents', kwargs={'pk': instance.pk}))

        if id_assisted:
            if form_assisted.is_valid():
                form_assisted.save()
                return HttpResponseRedirect(reverse('processes_update_documents', kwargs={'pk': instance.pk}))
            else:
                print(f'Esses são os erros = {form_assisted.errors}')
                return HttpResponseRedirect(reverse('processes_update_documents', kwargs={'pk': instance.pk}))

        if id_responsible:
            if form_responsible.is_valid():
                form_responsible.save()
                return HttpResponseRedirect(reverse('processes_update_documents', kwargs={'pk': instance.pk}))
            else:
                print(form_responsible.errors)
                return HttpResponseRedirect(reverse('processes_update_documents', kwargs={'pk': instance.pk}))


class ProcessesDelete(DeleteView):
    model = ProcessesModel
    template_name = 'processes_delete.html'
    success_url = '/processes/list/'

class ProcessesProtocolDetail(DetailView):
    model = ProcessesModel
    template_name = 'processes_protocol.html'


class ProcessNotesCreate(CreateView):
    template_name = 'processes_create_notes.html'
    model = ProcessesNotesModel
    form_class = ProcessesNotesForm


def open_document(request, pk):
    document_type = request.GET.get('type', '')  # Captura o tipo de documento da query string

    try:
        if document_type == 'assisted':
            document = AssistedDocumentModel.objects.get(pk=pk)
        elif document_type == 'responsibles':
            document = ResponsiblesDocumentsModel.objects.get(pk=pk)
        elif document_type == 'process':
            document = ProcessDocumentModel.objects.get(pk=pk)

        # Verifica se o documento tem um arquivo associado
        if document.file:
            file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))

            # Verifica se o arquivo realmente existe no sistema de arquivos
            if os.path.exists(file_path):
                try:
                    # Retorna o arquivo como uma resposta
                    return FileResponse(open(file_path, 'rb'),
                                        content_type='application/pdf')  # ou outro tipo relevante
                except FileNotFoundError:
                    print('Erro ao abrir o arquivo no sistema de arquivos.')
                    raise Http404("Documento não encontrado.")
            else:
                raise Http404("Arquivo não encontrado no sistema de arquivos.")
        else:
            raise Http404("Documento não possui um arquivo associado.")

    except AssistedDocumentModel.DoesNotExist:
        print('Documento do assistido não encontrado.')
        raise Http404("Documento do assistido não encontrado.")
    except ResponsiblesDocumentsModel.DoesNotExist:
        print('Documento do responsável não encontrado.')
        raise Http404("Documento do responsável não encontrado.")




