from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('', Principal.as_view(), name='index'),
    path('', Principal2.as_view(), name='index2'),
    path('paginaalter/producto/<int:pk>', Productos.as_view(), name='prducto'),
    path('paginaalter/contacto/', Contacto.as_view(), name='cont'),
    path('enviarCatalogo/', Catalogo.as_view(), name='cata'),
    # login
    path('accounts/login/', LoginFormView.as_view(), name='vista_login'),
    path('logout/', login_required(logoutUserSnout), name='vista_logout'),
]
