from django.shortcuts import render
from .forms import FormContatto
from django.http import HttpResponse
# Create your views here.

def contatti(request):
    #form=FormContatto()
    #context={"form": form}
    #return render(request, "contatto.html", context)
    if request.method == "POST": 
        form = FormContatto(request.POST) 
        if form.is_valid(): 
            print("Salvo il contatto nel database")
            nuovo_contato=form.save()
            print(nuovo_contato.nome)
            print (nuovo_contato.nomecognome)
            print(nuovo_contato.nome.email)
            print (nuovo_contato.nome.contenuto) 
            
            return HttpResponse("<h1>Grazie per averci contattato!</hl>")
        
    else: 
        form=FormContatto()
    
    context = {"form": form}
    return render(request, "contatto.html", context)