from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render, redirect
from .models import RequiredsModel
from .forms import RequiredsForm
from processes.forms import ProcessesForm
from responsibles.models import ResponsiblesModel


class RequiredsList(ListView):
    model = RequiredsModel
    template_name = 'requireds_list.html'
    context_object_name = 'requireds'

    def get_queryset(self):
        requireds = RequiredsModel.objects.all()
        search_required = self.request.POST.get('search-required', '')

        if search_required:
            requireds =requireds.filter(cpf__icontains=search_required)

        return requireds



class RequiredsCreate(CreateView):
    model = RequiredsModel
    form_class = RequiredsForm
    template_name = 'requireds_create.html'
    success_url = '/requireds/list/'



class RequiredsDetail(DetailView):
    model = RequiredsModel
    template_name = 'requireds_detail.html'


class RequiredsUpdate(UpdateView):
    model = RequiredsModel
    form_class = RequiredsForm
    template_name = 'requireds_update.html'
    success_url = '/requireds/list/'

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


class RequiredsUpdateProcesses(UpdateView):
    model = RequiredsModel
    form_class = RequiredsForm
    template_name = 'requireds_update_processes.html'


class RequiredsUpdateUnic(UpdateView):
    model = RequiredsModel
    form_class = RequiredsForm
    template_name = 'requireds_update_unic.html'
    success_url = '/requireds/list/'

class RequiredsDelete(DeleteView):
    model = RequiredsModel
    template_name = 'requireds_delete.html'
    success_url = '/requireds/list/'


