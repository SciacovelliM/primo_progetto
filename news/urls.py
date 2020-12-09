from django.urls import path
from.views import home, ArticoloDetailViewCB
app_name = 'news'
urlpatterns = [
    path('', home, name='homeview'),
    path('articoli/<int:pk>', ArticoloDetailViewCB.as_view(), name='articolo_detail')
    path('lista_articoli/', ArticoloListView.as_view(), name='lista_articoli')
]
