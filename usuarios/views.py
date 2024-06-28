import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        confirm_email = request.POST.get('confirm_email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Verifica se todos os campos obrigatórios estão preenchidos
        if not nome.strip() or not email.strip() or not password.strip():
            return redirect('/auth/cadastro/?status=1')  # Campos obrigatórios não preenchidos

        # Verifica se os e-mails coincidem
        if email != confirm_email:
            return redirect('/auth/cadastro/?status=2')  # E-mails não coincidem

        # Verifica se as senhas coincidem
        if password != confirm_password:
            return redirect('/auth/cadastro/?status=3')  # Senhas não coincidem
        
        # Verifica se a senha atende aos critérios especificados
        if not senha_valida(password):
            return redirect('/auth/cadastro/?status=4')  # Senha não atende aos critérios

        # Verifica se o e-mail já está em uso
        if Usuario.objects.filter(email=email).exists():
            return redirect('/auth/cadastro/?status=5')  # E-mail já em uso

        try:
            # Hash da senha usando SHA-256
            hashed_password = sha256(password.encode()).hexdigest()

            # Cria o usuário se todas as validações passaram
            usuario = Usuario(nome=nome, email=email, password=hashed_password)
            usuario.save()

            return redirect('/auth/cadastro/?status=0')  # Cadastro realizado com sucesso
        except Exception as e:
            # Trata outros erros inesperados
            print(f"Erro ao cadastrar usuário: {e}")
            return redirect('/auth/cadastro/?status=6')  # Erro desconhecido

    return redirect('/auth/cadastro/')

def senha_valida(senha):
    # Pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False

    # Pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False

    # Pelo menos um número
    if not re.search(r'\d', senha):
        return False

    # Pelo menos um caractere especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False

    return True


def valida_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    hashed_password = sha256(password.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email, password=hashed_password)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect(f'/menu/home/?id_usuario={request.session["usuario"]}')

def sair(request):
    request.session.flush()
    return redirect('/auth/login/')