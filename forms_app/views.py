from django.shortcuts import render
from .forms import FormContatto
# Create your views here.

def contatti(request):
    #form=FormContatto()
    #context={"form": form}
    #return render(request, "contatto.html", context)
    if request.method == "POST": 
        form = FormContatto(request.POST) 
        if form.is_valid(): 
            print("Il Form è Valido!") 
            print("NOME: ", form.cleaned_data["nome"])
            print ("COGNOME: ", form.cleaned_data ["cognome"])
            print("EMAIL: ", form.cleaned_datal["email"])
            print ("CONTENUTO: ", form.cleaned_data["contenuto"]) 
            
            return HttpResponse("<h1>Grazie per averci contattato!</hl>")
        
    else: 
        form=FormContatto()
    
    context = {"form": form}
    return render(request, "contatto.html", context)