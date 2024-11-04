from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView, DetailView
from cooperators.models import CooperatorsModel
from processes.models import ProcessesModel
from subs.forms import SubForm
from subs.models import SubModel
from django.http import HttpResponseRedirect


class SubList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'sub_list.html'
    model = SubModel
    context_object_name = 'subs'
    permission_required = 'subs.view_submodel'

    def get_queryset(self):
        subs = SubModel.objects.all()
        search_name = self.request.GET.get('search-name', '')
        search_number_process = self.request.GET.get('search-number-process','')
        search_protocol = self.request.GET.get('search-protocol', '')

        if search_name:
            subs = subs.filter(advocate_new__name__icontains=search_name)
        if search_number_process:
            subs = subs.filter(number_process=search_number_process)
        if search_protocol:
            subs = subs.filter(protocol=search_protocol)

        return subs

class SubSearchSub(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'sub_search_sub.html'
    model = ProcessesModel
    context_object_name = 'processes'
    permission_required = 'subs.view_submodel'

    def get_queryset(self):
        processes = ProcessesModel.objects.all()
        search_name = self.request.GET.get('search-name', '')
        search_number_process = self.request.GET.get('search-number-process','')
        search_protocol = self.request.GET.get('search-protocol', '')

        if search_name:
            processes = processes.filter(id_advocate__name__icontains=search_name)
        if search_number_process:
            processes = processes.filter(number_process=search_number_process)
        if search_protocol:
            processes = processes.filter(protocol=search_protocol)

        return processes


class SubCreate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'sub_create.html'
    model = ProcessesModel
    form_class = SubForm
    success_url = '/sub/list/'
    permission_required = 'subs.change_submodel'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['cooperators'] = CooperatorsModel.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        protocol = request.POST.get('protocol', '')
        advocate_new = request.POST.get('advocate_new', '')
        advocate_new = CooperatorsModel.objects.filter(pk=advocate_new).first()
        form_data = {
            'protocol': protocol,
            'advocate_current': request.POST.get('advocate_current', ''),
            'advocate_new': advocate_new.name,
            'processes_number': request.POST.get('processes_number', ''),
            'reason': request.POST.get('reason', ''),
        }
        print(f'ID - {advocate_new}')
        form = self.form_class(data=form_data)
        if form.is_valid():
            if protocol:
                process = ProcessesModel.objects.filter(protocol=protocol).first()

                process.id_advocate = advocate_new
                process.save()
                form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            print(form.errors)
            return self.form_invalid(form)

class SubDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'sub_detail.html'
    model = SubModel
    permission_required = 'subs.view_submodel'




