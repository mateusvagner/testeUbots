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
        ##
        pesquisa = str(search_id)
        lista_pesquisa = pesquisa.split(', ')
        set_pesquisa = set(lista_pesquisa)
        
        filmes = Filme.objects.all()
        lista_filmes = [ filme.nome for filme in filmes]
        set_filmes = set(lista_filmes)
        
        #todo -> arrumar a saída do esquema.
        
        try:
            #movie = Filme.objects.get(nome = search_id)
            #html = (movie)
                     
            
            filmes_assistidos = [i for i in (set_pesquisa & set_filmes)]
            
            return HttpResponse(filmes_assistidos)
        
        except Filme.DoesNotExist:
            return HttpResponse("O filme não consta na lista de assistidos")  
    
    else:
        #return render(request, 'index_api.html')
        filmes = Filme.objects.all()
        return render(request, 'index_api.html', {'filmes': filmes})