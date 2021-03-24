from django.urls import path
from.views import LibroListCBV, AutoreDetailCBV
app_name = 'libreria'
urlpatterns = [
    path('libri', LibroListCBV.as_view(), name='listaTuttiLibri'),
    path('autore/<int:pk>/', AutoreDetailCBV.as_view(), name='profilo_autore'),
]
