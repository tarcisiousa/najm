from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

@login_required
def Login(TemplateView):
    template_name = 'login.html'

def login_view(request):
    error_message = None  # Variável para armazenar a mensagem de erro

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Primeiro, verifica se o usuário existe
        try:
            user = User.objects.get(username=username)
            # Verifica se o usuário está ativo
            if not user.is_active:
                error_message = "Sua conta está desativada. Entre em contato com o administrador."
            else:
                # Autentica o usuário
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home_list')
                else:
                    error_message = "Senha incorreta. Tente novamente."
        except User.DoesNotExist:
            error_message = "Nome de usuário não encontrado. Verifique e tente novamente."

    # Se for um GET ou houver erro, exibe o formulário de login e a mensagem de erro (se houver)
    login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form, 'error_message': error_message})



def logout_view(request):
    print('logout')
    logout(request)
    return redirect('home_list')






