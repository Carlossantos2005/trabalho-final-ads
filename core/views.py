from django.shortcuts import render
from .models import Produto, Categoria

def index(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    
    context = {
        'categorias': categorias,
        'produtos': produtos
    }
    return render(request, 'core/index.html', context)