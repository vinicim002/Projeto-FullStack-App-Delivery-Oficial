from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import ItemMenu, Categoria

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario']).nome
        return render(request, 'home.html', {'nome': usuario})
    else:
        if not request.session.get('carrinho'):
            request.session['carrinho'] = []
            request.session.save()
        itemMenu = ItemMenu.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'home.html', {
            'itemMenu': itemMenu,
            'carrinho': len(request.session['carrinho']),
            'categorias': categorias
        })
