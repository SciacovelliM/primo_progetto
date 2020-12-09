from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from.models import Articolo, Giornalista
from django.views.generic.detail import DetailView
# Create your views here.
#def home(request):
#    return HttpResponse("<h1>Homepage!</h1>")

def home(request):
    articoli=Articolo.objects.all()
    giornalisti= Giornalista.objects.all()
    context={"articoli": articoli, "giornalisti":giornalisti}
    print(context)
    return render(request, "homepage.html", context)

def articoloDetailView(request, pk):
    #articolo=Articolo.objects.get(pk=pk)
    articoli=get_object_or_404(Articolo, pk=pk)
    context={"articoli": articoli}
    print(context)
    return render(request, "articolo_detail.html", context)

class ArticoloDetailViewCB(DetailView):
    model=Articolo
    template_name="articolo_detail.html"