from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from assisteds.models import AssistedsModel


def get_assisted(request, search_assisted, template_name, ):
    if search_assisted:
        assisteds = AssistedsModel.objects.all()
        assisteds = assisteds.filter(cpf=search_assisted).first()

        print(f'CPF do Assistido {search_assisted}')
        if assisteds:

            print(f'Acessando  {assisteds}')
            print(assisteds.pk)
            url_reverse = reverse('assisteds_update_search', kwargs={'pk': assisteds.pk})
            return HttpResponseRedirect(url_reverse)
        else:
            print('error 2')
            messages.error(request, 'Não existe registro com esse CPF.')
            return render(request, template_name, {
                'object': None,  # Corrigido para None, pois object não foi definido
                'error_message': 'Não existe registro com esse CPF.',
            })
    else:
        messages.error(request, 'Não existe registro com esse CPF.')
        return render(request, template_name, {
            'object': None,  # Corrigido para None, pois object não foi definido
            'error_message': 'Não existe registro com esse CPF.',
        })


def get_assisted_incapaz(request, search_assisted, template_name, ):
    if search_assisted:
        assisteds = AssistedsModel.objects.all()
        assisteds = assisteds.filter(cpf=search_assisted).first()
        if assisteds:
            url_reverse = reverse('assisteds_update_search_incapaz', kwargs={'pk': assisteds.pk})
            return HttpResponseRedirect(url_reverse)
        else:
            messages.error(request, 'Não existe registro com esse CPF.')
            return render(request, template_name, {
                'object': None,  # Corrigido para None, pois object não foi definido
                'error_message': 'Não existe registro com esse CPF.',
            })
    else:
        messages.error(request, 'Não existe registro com esse CPF.')
        return render(request, template_name, {
            'object': None,  # Corrigido para None, pois object não foi definido
            'error_message': 'Não existe registro com esse CPF.',
        })