from django.contrib import messages
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import CooperatorsModel
from .forms import CooperatorsForms
from processes.models import ProcessesModel


class CooperatorsList(ListView):
    model = CooperatorsModel
    template_name = 'cooperators_list.html'
    context_object_name = 'cooperators'

    def get_queryset(self):
        cooperators = CooperatorsModel.objects.all()
        search_cooperator = self.request.GET.get('search-cooperator', '')
        print(search_cooperator)

        if search_cooperator:
            cooperators = cooperators.filter(name__icontains=search_cooperator)

        return cooperators


class CooperatorsCreate(CreateView):
    model = CooperatorsModel
    form_class = CooperatorsForms
    template_name = 'cooperators_create.html'
    success_url = '/cooperators/list/'

    def form_valid(self, form):
        print('Deu certo')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class CooperatorsDetail(DetailView):
    model = CooperatorsModel
    template_name = 'cooperators_detail.html'


class CooperatorsUpdate(UpdateView):
    model = CooperatorsModel
    form_class = CooperatorsForms
    template_name = 'cooperators_update.html'
    success_url = '/cooperators/list/'


class CooperatorsDelete(DeleteView):
    model = CooperatorsModel
    template_name = 'cooperators_delete.html'
    success_url = '/cooperators/list/'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Obtenha o cooperador que está sendo excluído
        id_advocate = self.object.pk  # Pegue o ID do cooperador

        # Verifica se há algum processo relacionado ao cooperador
        if ProcessesModel.objects.filter(id_advocate=id_advocate).exists():
            # Se o cooperador está relacionado a processos, exibe a mensagem de erro e não exclui
            messages.error(self.request, 'O colaborador não pode ser excluído, pois está relacionado a processos.')
            return render(request, self.template_name, {
                'object': self.object,
                'error_message': 'O colaborador não pode ser excluído, pois está relacionado a processos.',
            })
        else:
            # Se não houver processos relacionados, permite a exclusão
            return super().post(request, *args, **kwargs)


