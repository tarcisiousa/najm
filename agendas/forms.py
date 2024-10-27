from django import forms
from .models import AgendaModel

class AgendaForm(forms.ModelForm):
    class Meta:
        model = AgendaModel
        fields = '__all__'

        widgets = {
            'id_assisted': forms.Select(attrs={
                "class": "h-8 px-2 rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm",
                "readonly": "readonly"
            }),
            'protocol': forms.TextInput(attrs={
                "class": "rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2",
                "readonly": "readonly", 'type': "hidden"
            }),
            'time_at': forms.Select(attrs={
                "class": "rounded-none rounded-e-lg bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"
            }),
        }