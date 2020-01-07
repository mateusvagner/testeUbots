from django.shortcuts import render
from .models import Filme
from django.shortcuts import HttpResponse

# Create your views here.
def Home(request):
    filmes = Filme.objects.all()
    return render(request, 'index_api.html', {'filmes': filmes})

def Search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
       
        pesquisa = str(search_id)
        lista_pesquisa = pesquisa.split(', ')
       
        filmes = Filme.objects.all()
        lista_filmes = [ filme.nome for filme in filmes]
        
        filmes_assistidos = [i for i, j in zip(lista_pesquisa, lista_filmes) if i == j]
        
                           
        return render(request, 'search_result.html', {'filmes': filmes_assistidos})  
    
    else:
        #return render(request, 'index_api.html')
        filmes = Filme.objects.all()
        return render(request, 'index_api.html', {'filmes': filmes})