from django.shortcuts import render

from django.views.generic import TemplateView, ListView, FormView
from .models import *
# login
from .forms import FormLogin
# librerias para la seguridad de la página
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import *
from django.urls import reverse_lazy


class Principal(TemplateView):
    template_name = 'index.html'


class Principal2(TemplateView):
    template_name = 'temp2/index.html'


class Productos(TemplateView):
    template_name = 'temp2/product.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        productos = Producto.objects.all()
        fotos = Prendas.objects.filter(id_producto_id=pk)
        return {'fotos': fotos, 'productos': productos}


class Contacto(TemplateView):
    template_name = 'temp2/contact.html'


class Catalogo(TemplateView):
    template_name = 'temp2/enviarCatalogo.html'


class LoginFormView(FormView):
    template_name = 'temp2/secion/login.html'
    form_class = FormLogin
    success_url = reverse_lazy('indexadmin')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginFormView, self).form_valid(form)


def logoutUserSnout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
