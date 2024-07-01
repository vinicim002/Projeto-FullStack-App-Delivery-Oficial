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

def add_carrinho(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()

    x = dict(request.POST)

    def removeLixo(adicional):
        adicionais = x.copy()
        adicionais.pop('id')
        adicionais.pop('csrfmiddlewaretoken')
        adicionais.pop('observacoes')
        adicionais.pop('quantidade')
        adicionais = list(adicionais.items())

        return adicionais
        
    adicionais = removeLixo(x)    


    id = int(x['id'][0])
    preco_total = Produto.objects.filter(id=id)[0].preco
    adicionais_verifica =  Adicional.objects.filter(produto = id)
    aprovado = True

    for i in adicionais_verifica:
        encontrou = False
        minimo = i.minimo
        maximo = i.maximo
        for j in adicionais:
            if i.nome == j[0]:
                encontrou = True
                if len(j[1]) < minimo or len(j[1]) > maximo:
                    aprovado = False
        if minimo > 0 and encontrou == False:
            aprovado = False
    
    if not aprovado:
        return redirect(f'/produto/{id}?erro=1')

    for i, j in adicionais:
        for k in j:
            preco_total += Opcoes.objects.filter(id=int(k))[0].acrecimo
    
    def troca_id_por_nome_adicional(adicional):
        adicionais_com_nome = []
        for i in adicionais:
            opcoes = []
            for j in i[1]:
                op = Opcoes.objects.filter(id = int(j))[0].nome
                opcoes.append(op) 
            adicionais_com_nome.append((i[0], opcoes))
        return adicionais_com_nome
    
    adicionais = troca_id_por_nome_adicional(adicionais)
    
    preco_total *= int(x['quantidade'][0])
    data = {'id_produto': int(x['id'][0]),
            'observacoes': x['observacoes'][0],
            'preco': preco_total,
            'adicionais': adicionais,
            'quantidade': x['quantidade'][0]}

    request.session['carrinho'].append(data)
    request.session.save()
    #return HttpResponse(request.session['carrinho'])
    return redirect(f'/ver_carrinho')