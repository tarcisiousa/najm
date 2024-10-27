from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

@login_required
def Login(TemplateView):
    template_name = 'login.html'


def login_view(request):
    auth_error = False
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_list')
        else:
            # Define a variável auth_error como True se a autenticação falhar
            auth_error = True
            login_form = AuthenticationForm()
    else:
        auth_error = False
        login_form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': login_form, 'auth_error': auth_error})



def logout_view(request):
    print('logout')
    logout(request)
    return redirect('home_list')


