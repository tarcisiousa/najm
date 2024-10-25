from django import forms
from .models import NotesModel


class NotesForm(forms.ModelForm):

    class Meta:
        model = NotesModel
        fields = '__all__'

        widgets = {
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