from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.defaulttags import csrf_token
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from datetime import date
from assisteds.models import AssistedsModel
from notes.models import NotesModel
from processes.models import ProcessesModel
from agendas.models import AgendaModel


class HomeTemplate(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = AgendaModel
    context_object_name = 'agendas'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        today = date.today().strftime('%d-%m-%Y')
        current_month = date.today().month
        agendas = AgendaModel.objects.all()
        register = AssistedsModel.objects.all()
        processes =ProcessesModel.objects.all()

        agendas_count = agendas.filter(date_at__month=current_month, status='1')
        notes = NotesModel.objects.filter(date_at=today)
        notes = notes.filter(status=0)
        register_count = register.filter(create_at__month=current_month)
        processes_finish_count = processes.filter(phase='ENCERRADO')

        context['agendas_count'] = agendas_count.count()
        context['notes'] = notes
        context['register_count'] = register_count.count()
        context['process_count'] = processes.count()
        context['processes_finish_count'] = processes_finish_count.count()
        return context

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            return redirect('assisteds_create')



