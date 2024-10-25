import os
from datetime import date

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404

from agendas.models import AgendaModel
from assisteds.models import AssistedsModel
from processes.models import ProcessesModel
from .models import ResponsiblesModel, ResponsiblesDocumentsModel
from .forms import ResponsiblesForm, ResponsiblesDocumentsForm
from requireds.models import RequiredsModel
from requireds.forms import RequiredsForm
from processes.forms import ProcessesForm
from django.utils.timezone import now
from agendas.forms import AgendaForm

class ResponsiblesList(ListView):
    model = ResponsiblesModel
    template_name = 'responsibles_list.html'
    context_object_name = 'responsibles'

    def get_queryset(self):
        responsibles = ResponsiblesModel.objects.all()
        search_responsible = self.request.GET.get('search-responsible', '')

        if search_responsible:
            responsibles = responsibles.filter(cpf__icontains=search_responsible)

        return responsibles


class ResponsiblesCreate(CreateView):
    model = ResponsiblesModel
    form_class = ResponsiblesForm
    template_name = 'responsibles_create.html'
    success_url = '/responsibles/list/'



class ResponsiblesDetail(DetailView):
    model = ResponsiblesModel
    template_name = 'responsibles_detail.html'


class ResponsiblesUpdate(UpdateView):
    model = ResponsiblesModel
    form_class = ResponsiblesForm
    template_name = 'responsibles_update.html'
    success_url = '/responsibles/list/'


    def form_valid(self, form):
        responsibles = self.get_object()
        responsibles_pk = responsibles.pk
        response = super().form_valid(form)

        return HttpResponseRedirect(reverse('responsibles_update_documents', kwargs={
            'pk': responsibles_pk}))

class ResponsiblesUpdateSearch(UpdateView):
    model = ResponsiblesModel
    form_class = ResponsiblesForm
    template_name = 'responsibles_update_search.html'
    success_url = '/responsibles/list/'

    def form_valid(self, form):
        print('form é válido')
        response = super().form_valid(form)
        today = now().strftime("%d-%m-%Y")
        id_assisted = self.request.POST.get('id_assisted', '')
        protocol = today.replace('-', '') + id_assisted
        post_data_processes = {
            'id_assisted': id_assisted,
            'protocol': protocol,
            'id_responsible': self.object.pk
        }
        post_data_agenda = {
            'id_assisted': id_assisted,
            'protocol': protocol,
            'status': '0',
        }
        processes_form = ProcessesForm(post_data_processes)
        agendas_form = AgendaForm(post_data_agenda)


        if processes_form.is_valid():
            print('segundo form é válido')
            saved_processes = processes_form.save()  # Salva o objeto e obtém a instância salva
            processes_pk = saved_processes.pk  # Obtém o pk da instância salva

            if agendas_form.is_valid():

                saved_agendas = agendas_form.save()
                agendas_pk = saved_agendas.pk

                return HttpResponseRedirect(reverse('agendas_update', kwargs={
                    'pk': agendas_pk}))  # Redireciona usando o pk do objeto recém-salvo
            else:
                print(agendas_form.errors)
        else:
            print(processes_form.errors)
        return response

class ResponsiblesUpdateUnic(UpdateView):
    model = ResponsiblesModel
    form_class = ResponsiblesForm
    template_name = 'responsibles_update_unic.html'
    success_url = '/responsibles/list/'

class ResponsiblesDelete(DeleteView):
    model = ResponsiblesModel
    template_name = 'responsibles_delete.html'
    success_url = '/responsibles/list/'

class ResponsiblesUpdateDocuments(UpdateView):
    model = ResponsiblesModel
    form_class = ResponsiblesDocumentsForm
    template_name = 'responsibles_update_documents.html'
    success_url = '/responsibles/list/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.object.pk)
        documents = ResponsiblesDocumentsModel.objects.filter(id_responsible=self.object.pk)
        context['documents'] = documents
        return context

    def post(self, request, *args, **kwargs):
        today = now().strftime("%d-%m-%Y")
        id_assisted = request.POST.get('id_assisted', '')
        id_responsible = kwargs['pk']
        advance = request.POST.get('next', '')
        protocol = today.replace('-', '') + str(id_assisted)
        pk_document = request.POST.get('delete-document', '')


        if advance == 'Avançar':
            assisted_instance = get_object_or_404(AssistedsModel, pk=id_assisted)
            responsible_instance = get_object_or_404(ResponsiblesModel, pk=id_responsible)
            form_processes = ProcessesModel(protocol=protocol, id_assisted=assisted_instance, id_responsible=responsible_instance)
            form_processes.save()

            form_agenda = AgendaModel(protocol=protocol, id_assisted=assisted_instance)
            form_agenda.save()
            form_agenda_pk = form_agenda.pk
            return HttpResponseRedirect(reverse('agendas_update', kwargs={'pk': form_agenda_pk}))

        # Delete document
        if pk_document:
            document = ResponsiblesDocumentsModel.objects.filter(pk=pk_document).first()
            if document and document.file:
                file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))
                # Verifica se o arquivo existe e o remove
                if os.path.exists(file_path):
                    os.remove(file_path)
                document.delete()
            return HttpResponseRedirect(reverse('responsibles_update_documents', kwargs={'pk': id_responsible}))

        # Add document
        form = self.get_form()
        if form.is_valid():
            document = form.save(commit=False)
            document.id_responsible_id = id_responsible
            document.save()
            return HttpResponseRedirect(reverse('responsibles_update_documents', kwargs={'pk': id_responsible}))
        else:
            print(form.errors)
            # Renderiza o template novamente com os erros do formulário
            return self.form_invalid(form)




