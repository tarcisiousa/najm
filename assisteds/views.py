import os
from datetime import date

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.utils.timezone import now
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from agendas.models import AgendaModel
from processes.models import ProcessesModel
from requireds.models import RequiredsModel
from responsibles.models import ResponsiblesModel
from . import metrics
from .models import AssistedsModel, AssistedDocumentModel
from .forms import AssistedsForm, AssistedsDocumentForm
from responsibles.forms import ResponsiblesForm
from requireds.forms import RequiredsForm


class AssistedsList(LoginRequiredMixin, ListView):
    model = AssistedsModel
    template_name = 'assisteds_list.html'
    context_object_name = 'assisteds'

    def get_queryset(self):
        assisteds = AssistedsModel.objects.all()
        search_assisted = self.request.GET.get('search-assisted', '')
        print(search_assisted)

        if search_assisted:
            assisteds = assisteds.filter(cpf__icontains=search_assisted)

        return assisteds


class AssistedsCreate(LoginRequiredMixin, CreateView):
    model = AssistedsModel
    model_doc = AssistedDocumentModel
    form_class = AssistedsForm
    form_class_doc = AssistedsDocumentForm
    template_name = 'assisteds_create.html'
    success_url = '/assisteds/list/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        condition_value = self.request.POST.get('condition', '')
        print(f'Condição - {condition_value}')
        search_assisted = self.request.POST.get('search-assisted', '')

        if search_assisted:
            request = self.request
            template_name = self.template_name
            return metrics.get_assisted(request, search_assisted, template_name)

        # Preenche o campo 'condition' do formulário com o valor recuperado
        form.data = form.data.copy()  # Faz uma cópia dos dados do formulário
        form.data['condition'] = condition_value.replace('c', 'C')  # Atribui o valor do HTML ao campo 'condition'

        if form.is_valid():
            assisted_instance = form.save()
            return HttpResponseRedirect(reverse('assisteds_update_documents', kwargs={'pk': assisted_instance.pk}))
        else:
            print(f'Condição - {condition_value}')
            print('Erro no formulário:', form.errors)

            return super().post(request, *args, **kwargs)

class AssistedsCreateIncapaz(LoginRequiredMixin, CreateView):
    model = AssistedsModel
    form_class = AssistedsForm
    template_name = 'assisteds_create_incapaz.html'
    success_url = '/assisteds/list/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        condition_value = self.request.POST.get('condition', '')
        search_assisted = self.request.POST.get('search-assisted', '')

        if search_assisted:
            request = self.request
            template_name = self.template_name
            return metrics.get_assisted_incapaz(request, search_assisted, template_name)

        # Preenche o campo 'condition' do formulário com o valor recuperado
        form.data = form.data.copy()  # Faz uma cópia dos dados do formulário
        form.data['condition'] = condition_value.replace('i', 'I')  # Atribui o valor do HTML ao campo 'condition'
        if form.is_valid():
            assisted_instance = form.save()
            return HttpResponseRedirect(reverse('assisteds_update_documents', kwargs={'pk': assisted_instance.pk}))
        else:
            print('Erro no formulário:', form.errors)
            return super().post(request, *args, **kwargs)

class AssistedsDetail(LoginRequiredMixin, DetailView):
    model = AssistedsModel
    template_name = 'assisteds_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        assisted = self.kwargs.get('pk')
        print(assisted)
        documents = AssistedDocumentModel.objects.filter(id_assisted=assisted)
        for i in documents:
            print(i.id_assisted.pk)

        context['documents'] = documents
        return context


class AssistedsUpdate(LoginRequiredMixin, UpdateView):
    model = AssistedsModel
    form_class = AssistedsForm
    template_name = 'assisteds_update.html'
    success_url = '/assisteds/list/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        assisted = self.kwargs.get('pk')
        documents = AssistedDocumentModel.objects.filter(id_assisted=assisted)
        context['documents'] = documents
        return context

class AssistedsUpdateSearch(LoginRequiredMixin, UpdateView):
    model = AssistedsModel
    form_class = AssistedsForm
    template_name = 'assisteds_update_search.html'
    success_url = '/assisteds/list/'

    def form_valid(self, form, *args, **kwargs):
        print('iniciou')
        self.object = self.get_object()
        today = date.today().strftime('%d%m%Y')
        agendas = AgendaModel.objects.all()
        new_agenda = AgendaModel(
            id_assisted=self.object,
            protocol=f'{today}{self.object.pk}',
            status='0',
        )
        new_agenda.save()
        return HttpResponseRedirect(reverse('agendas_update', kwargs={'pk': new_agenda.pk}))

    def form_invalid(self, form):
        print(form.errors)
        return HttpResponseRedirect(reverse('assisteds_update_search', kwargs={'pk': self.object.pk}))


class AssistedsUpdateSearchIcapaz(LoginRequiredMixin, UpdateView):
    model = AssistedsModel
    form_class = AssistedsForm
    template_name = 'assisteds_update_search_incapaz.html'
    success_url = '/assisteds/list/'

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        responsibles = ResponsiblesModel.objects.filter(id_assisted=self.object.id).first()
        return HttpResponseRedirect(reverse('responsibles_update_search', kwargs={'pk': responsibles.pk}))


class AssistedsUpdateDocuments(LoginRequiredMixin, UpdateView):
    model = AssistedsModel
    form_class = AssistedsDocumentForm
    template_name = 'assisteds_update_documents.html'
    success_url = '/assisteds/list/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        documents = AssistedDocumentModel.objects.filter(id_assisted=self.object.pk)
        context['documents'] = documents
        return context

    def post(self, request, *args, **kwargs):
        today = now().strftime("%d-%m-%Y")
        id_assisted = request.POST.get('id_assisted', '')
        advance = request.POST.get('next', '')
        protocol = today.replace('-', '') + str(id_assisted)
        pk_document = self.request.POST.get('delete-document', '')
        assisted_instance = get_object_or_404(AssistedsModel, pk=id_assisted)


        if advance == 'Avançar':
            if assisted_instance.condition == 'Capaz':
                form_processes = ProcessesModel(protocol=protocol, id_assisted=assisted_instance)
                form_processes.save()

                form_agenda = AgendaModel(protocol=protocol, id_assisted=assisted_instance)
                form_agenda.save()
                form_agenda_pk = form_agenda.pk
                return HttpResponseRedirect(reverse('agendas_update', kwargs={'pk': form_agenda_pk}))
            else:
                print(f'Assistido - `{assisted_instance}')

                form_responsibles = ResponsiblesModel(id_assisted=assisted_instance)
                form_responsibles.save()
                form_responsibles_pk = form_responsibles.pk
                return HttpResponseRedirect(reverse('responsibles_update', kwargs={'pk': form_responsibles_pk}))

        #delet document
        if pk_document:
            document = AssistedDocumentModel.objects.filter(pk=pk_document).first()

            if document and document.file:
                file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))

                # Verifica se o arquivo realmente existe no sistema de arquivos e o remove
                if os.path.exists(file_path):
                    os.remove(file_path)

            document.delete()

            return HttpResponseRedirect(reverse('assisteds_update_documents', kwargs={'pk': id_assisted}))

        #add
        form = self.get_form()
        form.id_assisted = id_assisted
        if form.is_valid():
            self.object = form.save()  # Salva o objeto e atualiza `self.object`
            print(f'Document adicionado - {self.object.pk}')
            # Redireciona para a URL de atualização com o ID do assistido
            return HttpResponseRedirect(reverse('assisteds_update_documents', kwargs={'pk': id_assisted}))
        else:
            print(form.errors)
            # Caso o formulário não seja válido, renderiza novamente o template com os erros
            return self.form_invalid(form)


class AssistedsDelete(LoginRequiredMixin, DeleteView):
    model = AssistedsModel
    template_name = 'assisteds_delete.html'
    success_url = '/assisteds/list/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_assisted = self.object.pk
        responsibles_exists = ResponsiblesModel.objects.filter(id_assisted=id_assisted).exists()
        requireds_exists = RequiredsModel.objects.filter(id_assisted=id_assisted).exists()
        if requireds_exists or responsibles_exists:
            messages.error(self.request, 'O requerente não pode ser excluído, pois está relacionado a processos ou requerido.')
            return render(request, self.template_name, {
                'object': self.object,
                'error_message': 'O requerente não pode ser excluído, pois está relacionado a processos ou requerido.',
            })
        else:
            return super().post(request, *args, **kwargs)




