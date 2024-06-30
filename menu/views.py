# views.py
from django.shortcuts import render
from usuarios.models import Usuario
from .models import ItemMenu, Categoria
from django.http import HttpResponse

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.filter(id=request.session['usuario']).first()
        if usuario:
            nome_usuario = usuario.nome
        else:
            nome_usuario = "Usuário Desconhecido"
        return render(request, 'home.html', {'nome': nome_usuario})
    else:
        if not request.session.get('carrinho'):
            request.session['carrinho'] = []
            request.session.save()
        itemMenus = ItemMenu.objects.filter(disponivel=True)  # Filtrar apenas os itens disponíveis
        categorias = Categoria.objects.all()

        return render(request, 'home.html', {
            'itemMenus': itemMenus,
            'carrinho': len(request.session['carrinho']),
            'categorias': categorias,
        })


def categorias(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    itemMenus = ItemMenu.objects.filter(categoria_id = id)
    categorias = Categoria.objects.all()

    return render(request, 'home.html', {'itemMenus': itemMenus,
                                        'carrinho': len(request.session['carrinho']),
                                        'categorias': categorias,})

def itemMenu(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    erro = request.GET.get('erro')
    itemMenu = ItemMenu.objects.filter(id=id)[0]
    categorias = Categoria.objects.all()
    return render(request, 'produto.html', {'itemMenu': itemMenu, 
                                            'carrinho': len(request.session['carrinho']),
                                            'categorias': categorias,
                                            'erro': erro})