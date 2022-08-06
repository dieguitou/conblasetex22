from django.urls import path
from .views import *

urlpatterns = [
    path('admin2', IndexA.as_view(), name='indexadmin'),
    path('mandarcorreo', RegistrarUsu.as_view(), name="mandar catalogo"),
    path('usuari/', ListarUsu.as_view(), name='listar_usuarios'),
    path('mandar/', mandarCorreo_.as_view(), name='mandarcorreo'),

]
