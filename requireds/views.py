from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect
from .models import RequiredsModel
from .forms import RequiredsForm
from processes.forms import ProcessesForm
from responsibles.models import ResponsiblesModel


class RequiredsList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = RequiredsModel
    template_name = 'requireds_list.html'
    context_object_name = 'requireds'
    permission_required = 'requireds.view_requiredsmodel'

    def get_queryset(self):
        requireds = RequiredsModel.objects.all()
        search_required = self.request.POST.get('search-required', '')

        if search_required:
            requireds =requireds.filter(cpf__icontains=search_required)

        return requireds

class RequiredsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = RequiredsModel
    form_class = RequiredsForm
    template_name = 'requireds_create.html'
    success_url = '/requireds/list/'
    permission_required = 'requireds.add_requiredsmodel'


class RequiredsDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = RequiredsModel
    template_name = 'requireds_detail.html'
    permission_required = 'requireds.view_requiredsmodel'


class RequiredsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = RequiredsModel
    form_class = RequiredsForm
    template_name = 'requireds_update.html'
    success_url = '/requireds/list/'
    permission_required = 'requireds.change_requiredsmodel'

    def form_valid(self, form):
        response = super().form_valid(form)
        id_required = self.request.POST.get('id_required', '')
        id_assisted = self.request.POST.get('id_assisted', '')
        id_resposibles = ResponsiblesModel.objects.filter(id_assisted=id_assisted).first()

        post_data = {
            'id_assisted': id_assisted,
            'id_responsible': id_resposibles,
            'id_required': id_required,
        }
        processes_form = ProcessesForm(post_data)
        if processes_form.is_valid():
            saved_processes = processes_form.save()
            processes_pk = saved_processes.pk
            return HttpResponseRedirect(reverse('processes_update', kwargs={'pk': processes_pk}))
        else:
            print(processes_form.errors)

        return response


class RequiredsUpdateProcesses(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = RequiredsModel
    form_class = RequiredsForm
    template_name = 'requireds_update_processes.html'
    permission_required = 'requireds.change_requiredsmodel'


class RequiredsUpdateUnic(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = RequiredsModel
    form_class = RequiredsForm
    template_name = 'requireds_update_unic.html'
    success_url = '/requireds/list/'
    permission_required = 'requireds.change_requiredsmodel'

class RequiredsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = RequiredsModel
    template_name = 'requireds_delete.html'
    success_url = '/requireds/list/'
    permission_required = 'requireds.delete_requiredsmodel'


