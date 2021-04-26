from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import render, redirect


def login(request):

    if request.method != 'POST':
        return render(request,'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    atenticacao = auth.authenticate(request, username=usuario, password=senha)

    if atenticacao:
        if atenticacao.is_staff:
            auth.login(request,atenticacao)
            messages.add_message(request, messages.SUCCESS, 'Logado com sucesso!')
            return redirect('dash_index')
        else:
            auth.login(request, atenticacao)
            messages.add_message(request, messages.SUCCESS, 'Logado com sucesso!')
            return redirect('dash_user_index')
    else:
        messages.add_message(request, messages.ERROR, 'Usuário ou senha inválidos!')
        return redirect('login')


def logout(request):
    auth.logout(request)
    messages.add_message(request,messages.INFO, 'Você saiu da sua conta')
    return redirect('super_index')


def novo_usuario(request):

    if request.method != 'POST':
        return render(request, 'accounts/novo_usuario.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    confirmacao = request.POST.get('confirmacao')

    if not nome or not sobrenome or not email or not usuario or not senha or not confirmacao:
        messages.add_message(request, messages.ERROR, 'Todos os campos são obrigatórios.')
        return render(request,'accounts/novo_usuario.html')

    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.ERROR, 'E-mail inválido.')
        return render(request,'accounts/novo_usuario.html')

    if len(senha)< 6:
        messages.add_message(request, messages.ERROR, 'Senha muito curta. Mínimo de 6.')
        return render(request,'accounts/novo_usuario.html')

    if senha != confirmacao:
        messages.add_message(request, messages.ERROR, 'Senhas não conferem.')
        return render(request, 'accounts/novo_usuario.html')

    if len(usuario)< 6:
        messages.add_message(request, messages.ERROR, 'Usuário muito curto. Mínimo de 6.')
        return render(request,'accounts/novo_usuario.html')

    if User.objects.filter(username= usuario).exists():
        messages.add_message(request, messages.ERROR, 'Usuário já cadastrado.')
        return render(request, 'accounts/novo_usuario.html')

    if User.objects.filter(email= email).exists(): #verificção de email
        messages.add_message(request, messages.ERROR, 'E-mail já cadastrado.')
        return render(request, 'accounts/novo_usuario.html')

    messages.add_message(request, messages.SUCCESS, 'Usuário cadastrado com sucesso. Agora faça o login')
    user = User.objects.create_user(username=usuario, email= email, password= senha,
                                    first_name=nome, last_name= sobrenome)
    user.save()
    return redirect('login')

