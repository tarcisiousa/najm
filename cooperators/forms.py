from django import forms
from .models import CooperatorsModel


class CooperatorsForms(forms.ModelForm):
    class Meta:
        model = CooperatorsModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'post': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'registration': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'number_order': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'email': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'fone_1': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'fone_2': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'address': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'district': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'city': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'uf': forms.Select(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),
            'cpf': forms.TextInput(attrs={
                "class": "h-6 mt-1 rounded-none w-full px-2 rounded-l-md rounded-r-md bg-gray-50 border border-blue-800 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 text-sm mr-2"}),

        }
        labels = {
            'name': 'Nome Completo',
            'post': 'Cargo',
            'cpf': 'CPF',
            'number_order': 'Número da Ordem',
            'email': 'E-mail',
            'fone_1': 'Telefone Principal',
            'fone_2': 'Telefone Alternativo',
            'address': 'Endereço',
            'district': 'Bairro',
            'city': 'Cidade',
            'uf': 'UF',
        }

    def __init__(self, *args, user=None, **kwargs):
        super(CooperatorsForms, self).__init__(*args, **kwargs)
        if self.instance.pk:  # Verifica se já existe uma instância
            if user and not user.groups.filter(name='Administrador(a)').exists():  # Verifica se o usuário não é do grupo de administradores
                self.fields['post'].choices = [choice for choice in self.fields['post'].choices if choice[0] == self.instance.post]

