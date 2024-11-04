from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group, User
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from . import metrics
from .metrics import create_user_with_group
from .models import CooperatorsModel
from .forms import CooperatorsForms
from processes.models import ProcessesModel


class CooperatorsList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CooperatorsModel
    template_name = 'cooperators_list.html'
    context_object_name = 'cooperators'
    permission_required = 'cooperators.view_cooperatorsmodel'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passa o usuário atual
        return kwargs

    def get_queryset(self, *args, **kwargs):
        username = self.request.user.username
        groups = Group.objects.all()
        group_user = self.request.user.groups.first()
        cooperators = CooperatorsModel.objects.all()

        if str(group_user) == 'Administrador(a)':
            cooperators = CooperatorsModel.objects.all()
            search_cooperator = self.request.GET.get('search-cooperator', '')
            if search_cooperator:
                cooperators = cooperators.filter(name__icontains=search_cooperator)
        else:
            cooperators = cooperators.filter(cpf=username)


        return cooperators

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        users = User.objects.all()
        context['users'] = users

        return context


class CooperatorsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CooperatorsModel
    form_class = CooperatorsForms
    template_name = 'cooperators_create.html'
    success_url = '/cooperators/list/'
    permission_required = 'cooperators.add_cooperatorsmodel'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        groups = Group.objects.all()
        context['groups'] = groups
        return context

    def form_valid(self, form):
        data_user = form.cleaned_data
        username = self.request.POST.get('username', '')
        password = self.request.POST.get('password', '')
        request = self.request
        metrics.create_user_with_group(request, data_user, username, password)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class CooperatorsDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CooperatorsModel
    template_name = 'cooperators_detail.html'
    permission_required = 'cooperators.view_cooperatorsmodel'


class CooperatorsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CooperatorsModel
    form_class = CooperatorsForms
    template_name = 'cooperators_update.html'
    success_url = '/cooperators/list/'
    permission_required = 'cooperators.change_cooperatorsmodel'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passa o usuário atual
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cooperator = self.get_object()
        users_coop = User.objects.all()
        user_activate = users_coop.filter(username=cooperator.cpf).first()
        context['users_coop'] = users_coop
        context['user_active'] = user_activate.is_active
        print(users_coop)
        return context

    def form_valid(self, form):
        data_user = form.cleaned_data
        group_user = self.request.user.groups.first()
        username = self.request.POST.get('username', '')
        password = self.request.POST.get('password', '')
        user_active = self.request.POST.get('user_active', '')
        request = self.request

        if user_active:
            print('oi')
            cooperator = self.get_object()
            user = User.objects.filter(username=data_user.get('cpf')).first()
            if user.is_active == True:

                user.is_active = False
                user.save()
                print(f'True: {user.is_active}')
                return HttpResponseRedirect(reverse('cooperators_update', kwargs={'pk':cooperator.pk}))
            else:

                user.is_active = True
                user.save()
                print(f'False: {user.is_active}')
                return HttpResponseRedirect(reverse('cooperators_update', kwargs={'pk':cooperator.pk}))


        if self.request.user.username == form.instance.cpf:
            metrics.update_user_password(data_user, request, username, password)

        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)



class CooperatorsUpdateUnic(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CooperatorsModel
    form_class = CooperatorsForms
    template_name = 'cooperators_update_unic.html'
    success_url = '/cooperators/list/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        name = User.objects.username
        print(name)
        return context

class CooperatorsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CooperatorsModel
    template_name = 'cooperators_delete.html'
    success_url = '/cooperators/list/'
    permission_required = 'cooperators.delete_cooperatorsmodel'

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


