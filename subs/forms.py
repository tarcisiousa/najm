from django import forms
from .models import SubModel


class SubForm(forms.ModelForm):
    class Meta:
        model = SubModel
        fields = '__all__'

        widgets = {
            'number_processes': forms.Select(attrs={
                "class": "h-6 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'advocate_current': forms.Select(attrs={
                "class": "h-6 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'advocate_new': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'reason': forms.Textarea(attrs={
                "class": "rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
             }

