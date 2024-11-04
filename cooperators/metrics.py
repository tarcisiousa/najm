from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.contrib import messages

def create_user_with_group(request, data_user, username, password):
    # Dados de exemplo para criação do usuário
    username = username
    password = password
    email = data_user.get('email')
    name = data_user.get('name')

    # Cria o usuário
    user = User.objects.create_user(username=username, password=password, email=email, first_name=name)

    # Verifica se o grupo existe e adiciona o usuário ao grupo
    group_name = data_user.get('post')
    try:
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        messages.success(request, "Usuário criado e adicionado ao grupo com sucesso!")
        print("Usuário criado e adicionado ao grupo com sucesso!")
    except Group.DoesNotExist:
        messages.error(request, f"Grupo '{group_name}' não existe.")
        print(f"Grupo '{group_name}' não existe.")

    return redirect('cooperators_create')


def update_user_password(data_user, request, username, password):
    user = User.objects.filter(username=data_user.get('cpf')).first()
    if user:
        # Atualiza a senha do usuário
        if password:
            user.set_password(password)
        user.username = username
        user.save()  # Salva as alterações
        messages.success(request, "Senha atualizada com sucesso!")
    else:
        messages.error(request, f"Usuário '{username}' não encontrado.")

    return redirect('cooperators_create')
