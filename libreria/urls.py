from django.urls import path
from.views import LibroListCBV
app_name = 'libreria'
urlpatterns = [
    path('', LibroListCBV, name='lista_libri'),
]
