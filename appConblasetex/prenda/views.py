from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from .models import Prendas


class Principal(TemplateView):
    template_name = 'index.html'


class Principal2(TemplateView):
    template_name = 'temp2/index.html'


class Producto(ListView):
    template_name = 'temp2/product.html'
    model = Prendas
    context_object_name = 'fotos'
    queryset = Prendas.objects.all()


class Contacto(TemplateView):
    template_name = 'temp2/contact.html'


class Catalogo(TemplateView):
    template_name = 'temp2/enviarCatalogo.html'
