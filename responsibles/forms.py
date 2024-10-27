from django import forms
from .models import ResponsiblesModel, ResponsiblesDocumentsModel


class ResponsiblesForm(forms.ModelForm):
    class Meta:
        model = ResponsiblesModel
        fields = '__all__'

        widgets = {
            'id_assisted': forms.Select(attrs={
                "class": "h-6 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'kin': forms.Select(attrs={
                "class": "h-6 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'name': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'status_civil': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'nis': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'rg': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'organ': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'date_birth': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'date_expedition': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'cpf': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'email': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'fone_1': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'fone_2': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'address': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'district': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'city': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'uf': forms.Select(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'dad': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'mother': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'employee': forms.Select(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'salary': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'other_income': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'dependents': forms.TextInput(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
            'house': forms.Select(attrs={
                "class": "h-6  rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm -2"}),
        }

        labels = {
            'id_assisted': 'Assistido:',
            'kin': 'Grau de Parentesco:',
            'name': 'Nome Responsável:',
            'status_civil': 'Estado Civil:',
            'rg': 'RG:',
            'organ': 'Orgão Expedidor:',
            'date_birth': 'Data de Nascimento:',
            'cpf': 'CPF:',
            'email': 'E-mail:',
            'fone_1': 'Telefone 1:',
            'fone_2': 'Telefone 2:',
        }


class ResponsiblesDocumentsForm(forms.ModelForm):
    class Meta:
        model = ResponsiblesDocumentsModel
        fields = '__all__'

        widgets = {
            'id_responsible': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'type_document': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'file': forms.ClearableFileInput(attrs={
                "class": "mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'name_customize': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
        }