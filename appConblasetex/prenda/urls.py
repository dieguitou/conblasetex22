from django.contrib import admin
from django.urls import path
from .views import Principal, Principal2, Producto, Contacto, Catalogo

urlpatterns = [
    path('', Principal.as_view(), name='index'),
    path('paginaalter/', Principal2.as_view(), name='index2'),
    path('paginaalter/producto/', Producto.as_view(), name='prducto'),
    path('paginaalter/contacto/', Contacto.as_view(), name='cont'),
    path('enviarCatalogo/', Catalogo.as_view(), name='cata'),
]
