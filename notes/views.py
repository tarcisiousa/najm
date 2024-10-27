from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import NotesModel
from .forms import NotesForm


class NotesList(LoginRequiredMixin, ListView):
    template_name = 'notes_list.html'
    model = NotesModel
    context_object_name = 'notes'


class NotesCreate(LoginRequiredMixin, CreateView):
    template_name = 'notes_create.html'
    model = NotesModel
    form_class = NotesForm
    success_url = '/notes/list/'

    def form_valid(self, form):
        print('deu certo')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)  # Correção aqui


class NotesDetail(LoginRequiredMixin, DetailView):
    template_name = 'notes_detail.html'
    model = NotesModel

    def post(self, *args, **kwargs):
        pk_note = self.request.POST.get('pk-note')
        notes = NotesModel.objects.filter(pk=pk_note).first()

        if notes:
            notes.status = '1'
            notes.save()

        return redirect('home_list')



class NotesUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'notes_update.html'
    model = NotesModel
    form_class = NotesForm
    success_url = '/notes/list/'

    def form_valid(self, form):
        finish = self.request.POST.get('finish', '')

        note = form.save(commit=False)  # Evita salvar imediatamente
        if finish:
            note.status = '1'  # Atualiza o status da nota
        note.save()  # Salva as alterações no banco de dados

        return super().form_valid(form)


class NotesDelete(LoginRequiredMixin, DeleteView):
    template_name = 'notes_delete.html'
    model = NotesModel
    success_url = '/notes/list/'


