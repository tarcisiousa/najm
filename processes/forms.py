from django import forms
from .models import ProcessesModel, ProcessDocumentModel, ProcessesNotesModel


class ProcessesForm(forms.ModelForm):
    class Meta:
        model = ProcessesModel
        fields = '__all__'

        widgets = {
            'id_advocate': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'id_assisted': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'id_responsible': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'id_required': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'facts': forms.Textarea(attrs={
                "class": "mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'phase': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'number_process': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'jurisdiction': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'processes_matter': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'processes_classs': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'processes_subject': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
        }

        labels = {
            'id_advocate': 'Advogado(a):',
            'id_assisted': 'Requerente:',
            'id_responsible': 'Responsável:',
            'id_required': 'Requerido:',
            'facts': 'Fatos / Narrativa:',
            'number_process': 'Número do Processo',
            'phase': 'Fase:',
            'action': 'Ação:',
            'processes_matter':'Matéria:',
            'processes_classs': 'Classe:',
            'processes_subject': 'Assunto:'
        }

class ProcessesDocumentForm(forms.ModelForm):
    class Meta:
        model = ProcessDocumentModel
        fields = '__all__'

        widgets = {
            'id_process': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'type_document': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'file': forms.ClearableFileInput(attrs={
                "class": "mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'name_customize': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
        }


class ProcessesNotesForm(forms.ModelForm):

    class Meta:
        model = ProcessesNotesModel
        fields = '__all__'

    def clean_notes(self):
        notes = self.cleaned_data.get('notes')
        if notes is None or notes == '':
            return 0  # Retorna 0 se o campo estiver vazio
        return notes

        widgets = {
            'id_process': forms.TextInput(attrs={
                "class": "h-6 rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'subject': forms.TextInput(attrs={
                    "class": "h-6 rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'note': forms.Textarea(attrs={
                    "class": "px-2 rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'user': forms.TextInput(attrs={
                "class": "h-6 rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'priority': forms.Select(attrs={
                "class": "h-6 px-2 rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'date_at':forms.TextInput(attrs={
                "class": "h-6 rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'time_at': forms.TextInput(attrs={
                "class": "h-6 rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
        }

