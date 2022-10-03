from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect, get_object_or_404

from .models import RegistrarUsuario, CorreosHistorial

import smtplib
from email.mime.text import MIMEText
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import *
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import *
# correos
from django.core.mail import EmailMultiAlternatives
from django.template import loader

# BUSCAR
from django.db.models import Q
from appConblasetex.prenda.models import Producto
from appConblasetex.epp.models import Epp
from datetime import datetime


# Create your views here.
class IndexA(TemplateView):
    template_name = 'temp2/indexadmin.html'

    def get_context_data(self, **kwargs):
        productos_prenda = Producto.objects.filter(tipo='Prenda')
        productos_epp = Producto.objects.filter(tipo='EPP')
        return {'producto_prenda': productos_prenda, 'producto_epp': productos_epp}


# Nueva vista mejorada en el admin
class ListarPrendas(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        producto = Producto.objects.get(id=pk)
        productos_prenda = Producto.objects.filter(tipo='Prenda')
        productos_epp = Producto.objects.filter(tipo='EPP')
        prendas = Prendas.objects.filter(id_producto=pk)
        search = request.GET.get('search')

        if search:
            prendas = Prendas.objects.filter(
                Q(id_producto=pk) & (
                        Q(nombre__icontains=search) | Q(tipoTela__contains=search) | Q(color__icontains=search))
            )

        return render(request, 'temp2/producto.html',
                      {'prendas': prendas, 'producto': producto, 'producto_prenda': productos_prenda,
                       'producto_epp': productos_epp})


# new
class RegistrarUsu(View):
    @staticmethod
    def post(request):
        nombre = request.POST['txtNombreusu']
        corre = request.POST['txtcorreo']
        mensaje = request.POST['txtmensaje']
        RegistrarUsuario.objects.create(nombreUsu=nombre, correousu=corre, mensaje=mensaje)
        return redirect('cont')


# fin de vistas nuevas
class ListarUsu(TemplateView):
    template_name = 'temp2/enviarCatalogo.html'

    def get_context_data(self, **kwargs):
        usuarios3 = RegistrarUsuario.objects.all()
        productos_prenda = Producto.objects.filter(tipo='Prenda')
        productos_epp = Producto.objects.filter(tipo='EPP')
        correos = RegistrarUsuario.objects.all().values('correousu')
        for c in correos:
            print(c)
        return {'usuarios3': usuarios3, 'correos': correos, 'producto_prenda': productos_prenda,
                'producto_epp': productos_epp}


# new
class Registrar(View):
    def get(self, request, **kwargs):
        pk = self.kwargs['pk']
        producto = Producto.objects.get(id=pk)
        return render(request, 'temp2/modales/registrarChaleco.html', {'producto': producto})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        producto = Producto.objects.get(id=pk)
        nombre = request.POST['nombretxt']
        tela = request.POST['telatxt']
        color = request.POST['colortxt']
        talla = request.POST['tallatxt']
        descripcion = request.POST['descripciontxt']
        precio = request.POST['precionum']
        imagen = request.FILES['imagefil']
        fecha = request.POST['fechadate']
        if str(fecha) == "":
            fecha = None
        cantidad = request.POST['cantidad']
        Prendas.objects.create(nombre=nombre, tipoTela=tela, color=color, talla=talla,
                               descripcion=descripcion, precio=precio, imagen=imagen, fecha=fecha, cantidad=cantidad,
                               id_producto_id=producto.id)

        messages.success(request, "producto registrado")
        return redirect('vista_producto_prenda', producto.id)


# new
class Registrarv1(View):
    def get(self, request, **kwargs):
        pk = self.kwargs['pk']
        producto = Producto.objects.get(id=pk)
        return render(request, 'temp2/modales/registrarEpp.html', {'producto': producto})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        producto = Producto.objects.get(id=pk)
        nombre = request.POST['nombretxt']
        tela = ""
        color = request.POST['colortxt']
        talla = request.POST['tallatxt']
        descripcion = request.POST['descripciontxt']
        precio = request.POST['precionum']
        imagen = request.FILES['imagefil']
        fecha = request.POST['fechadate']
        cantidad = request.POST['cantidad']
        Prendas.objects.create(nombre=nombre, tipoTela=tela, color=color, talla=talla,
                               descripcion=descripcion, precio=precio, imagen=imagen, fecha=fecha, cantidad=cantidad,
                               id_producto_id=producto.id)

        messages.success(request, "producto registrado")
        return redirect('vista_producto_prenda', producto.id)


class RegistrarEpp(View):
    def get(self, request, **kwargs):
        pk = self.kwargs['pk']
        producto = Producto.objects.get(id=pk)
        return render(request, 'temp2/modales/registrarChaleco.html', {'producto': producto})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        producto = Producto.objects.get(id=pk)
        nombre = request.POST['nombretxt']
        tela = request.POST['telatxt']
        color = request.POST['colortxt']
        talla = request.POST['tallatxt']
        descripcion = request.POST['descripciontxt']
        precio = request.POST['precionum']
        imagen = request.FILES['imagefil']
        fecha = request.POST['fechadate']
        cantidad = request.POST['cantidad']
        Prendas.objects.create(nombre=nombre, tipoTela=tela, color=color, talla=talla,
                               descripcion=descripcion, precio=precio, imagen=imagen, fecha=fecha, cantidad=cantidad,
                               id_producto_id=producto.id)

        messages.success(request, "producto registrado")
        return redirect('vista_producto_prenda', producto.id)


# listar vitacora
class ListarVita(TemplateView):
    template_name = 'temp2/vistaprod/VistaVitacora.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        detalles = CorreosHistorial.objects.filter(id_registrousuario_id=pk)
        return {'detalles': detalles}


def eliminar_producto(request, id):
    # prenda1 = get_object_or_404(Prendas, id=id)
    prenda1 = Prendas.objects.get(id=id)
    producto = prenda1.id_producto_id
    productos = Producto.objects.get(id=producto)
    prenda1.delete()
    messages.info(request,
                  "El producto de la categoria" + " " + productos.nombre + " de nombre " + prenda1.nombre + " " + "fue eliminado")
    return redirect("vista_producto_prenda", producto)


def eliminar_Prod_Edd(request, id):
    productos = Producto.objects.get(id=id)
    productos.delete()
    messages.info(request, "El producto" + " " + productos.nombre + " " + "fue eliminado")
    return redirect("Agragar_prod")


# Adicionar producto
class AdicionarProd(TemplateView):
    template_name = 'temp2/vistaprod/AdicionarPorducto.html'

    def get_context_data(self, **kwargs):
        productos_prenda = Producto.objects.filter(tipo='Prenda')
        productos_epp = Producto.objects.filter(tipo='EPP')
        productos = Producto.objects.all().order_by('tipo')
        return {'productos': productos, 'producto_prenda': productos_prenda,
                'producto_epp': productos_epp}


# new agregar prenda
class RegistrarPrendaEpp(View):
    def get(self, request, **kwargs):
        return render(request, 'temp2/modales/registerPrendaEpp.html')

    def post(self, request, *args, **kwargs):
        nombre = request.POST['nombretxt']
        tipo = request.POST['tipotxt']
        Producto.objects.create(nombre=nombre, tipo=tipo)
        messages.success(request, "producto registrado")
        return redirect('Agragar_prod')


# correo new 2
class Mandarcorreo2(View):
    def post(self, request, *args, **kwargs):
        correos = RegistrarUsuario.objects.all()
        file = request.FILES['file']
        nombre_archivo = str(file.name)
        mensajee = []
        for correo in correos:
            historiales = CorreosHistorial.objects.filter(id_registrousuario=correo.id)
            swith = False
            if historiales.exists():
                for historial in historiales:
                    if historial.nombreArchi == nombre_archivo:
                        swith = True
                        break
            if swith == False:
                mensajee.append(str(correo.correousu))
        for mensage in mensajee:
            registro = RegistrarUsuario.objects.get(correousu=mensage)
            fecha = datetime.today().strftime('%Y-%m-%d')
            historial2 = CorreosHistorial.objects.create(nombreArchi=nombre_archivo, fechaArach=fecha,
                                                         id_registrousuario_id=registro.id)
            historial2.save()

        name = 'Confecciones Blanco y Segurida Textil'
        email = 'Conblasetex@gmail.com'
        message = "Hola estimado usuario"
        subject = "envio de archivos"
        template = loader.get_template('temp2/contact_forms.txt')
        context = {
            'name': name,
            'email': email,
            'message': message,
            'subject': subject,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            "tienes una promoción!", message,
            "CONFECCIONES BLANCO " + "Y SEGURIDAD TEXTIL",
            mensajee
        )
        email.content_subtype = 'html'

        email.attach(file.name, file.read(), file.content_type)
        email.send()
        print('envio correcto')
        messages.success(request, "mensaje enviado")
        return redirect('listar_usuarios')


class ListarPrenda(View):
    template_name = 'temp2/chaleco.html'

    def get(self, request):
        chalecos = Prendas.objects.filter(nombre__startswith="chaleco") | Prendas.objects.filter(
            nombre__startswith="Chaleco")
        return render(request, self.template_name, {'chalecos': chalecos})

    def post(self, request):
        busqueda = request.POST['buscar']
        chalecos = Prendas.objects.filter(nombre__startswith="chaleco") | Prendas.objects.filter(
            nombre__startswith="Chalecos")

        if busqueda:
            chalecos = Prendas.objects.filter(
                Q(nombre__icontains=busqueda) |
                Q(tipoTela__icontains=busqueda) |
                Q(color__icontains=busqueda) |
                Q(talla__icontains=busqueda)
            ).distinct()
        return render(request, self.template_name, {'chalecos': chalecos})


class CreatePrenda(View):
    def post(self, request):
        nombre = request.POST['nombretxt']
        tela = request.POST['telatxt']
        color = request.POST['colortxt']
        talla = request.POST['tallatxt']
        caracteristica = request.POST['caracteristicatxt']
        descripcion = request.POST['descripciontxt']
        precio = request.POST['precionum']
        imagen = request.FILES['imagefil']
        fecha = request.POST['fechadate']
        stock = request.POST['stock']
        Prendas.objects.create(nombre=nombre, tipoTela=tela, color=color, talla=talla, caracteristica=caracteristica,
                               descripcion=descripcion, precio=precio, imagen=imagen, fecha=fecha, stock=stock)

        messages.success(request, "producto registrado")
        return redirect('vista_listar')


# chamarras
class Chamarras(TemplateView):
    template_name = "temp2/chamarra.html"

    def get(self, request):
        chamarras = Prendas.objects.filter(nombre__startswith="chamarra") | Prendas.objects.filter(
            nombre__startswith="Chamarra")
        return render(request, self.template_name, {'chamarras': chamarras})

    def post(self, request):
        busqueda = request.POST['buscar']
        chamarras = Prendas.objects.filter(nombre__startswith="chamarra") | Prendas.objects.filter(
            nombre__startswith="Chamarra")

        if busqueda:
            chamarras = Prendas.objects.filter(
                Q(nombre__icontains=busqueda) |
                Q(tipoTela__icontains=busqueda) |
                Q(color__icontains=busqueda) |
                Q(talla__icontains=busqueda)

            ).distinct()
        return render(request, 'temp2/chamarra.html', {'chamarras': chamarras})


def eliminar_chamarra(request, id):
    prenda1 = get_object_or_404(Prendas, id=id)
    prenda1.delete()
    messages.success(request, "El productoaaa" + " " + prenda1.nombre + " " + "fue eliminado")
    return redirect(to="vista_chamarra")


# new editar chamarra
class Editarprenda2(UpdateView):
    model = Prendas
    template_name = 'temp2/modales/editarChamarra.html'
    form_class = PrendaForms
    success_url = reverse_lazy('vista_producto_prenda')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        objeto = Prendas.objects.get(id=pk)
        form = self.get_form()
        form.save()
        messages.success(request, "producto editado")
        return redirect('vista_producto_prenda', objeto.id_producto_id)


# new editar epp
class EditarEpp(UpdateView):
    model = Prendas
    template_name = 'temp2/modales/editarEpp.html'
    form_class = PrendaFormsv1
    success_url = reverse_lazy('vista_producto_prenda')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        objeto = Prendas.objects.get(id=pk)
        form = self.get_form()
        form.save()
        messages.success(request, "producto editado")
        return redirect('vista_producto_prenda', objeto.id_producto_id)


# new editar cantidad
class EditarCantidad(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        objeto = Prendas.objects.get(id=pk)
        return render(request, 'temp2/modales/editarCantidad.html', {'objeto': objeto})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        cantidad = request.POST['cantidad']
        objeto = Prendas.objects.get(id=pk)
        objeto.cantidad = objeto.cantidad + (int(cantidad))
        objeto.save()
        return redirect('vista_producto_prenda', objeto.id_producto_id)


# new vita

# new editar prendaEpp
class EditarprendaEpp(UpdateView):
    model = Producto
    template_name = 'temp2/modales/editarPrendasEpp.html'
    form_class = PrendaEppForms

    success_url = reverse_lazy('Agragar_prod')


##login


# detalles de imagenes
class VistaDetalles(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        producto = Prendas.objects.get(id=pk)
        return render(request, 'temp2/vistaprod/chamarraVista.html', {'producto': producto})


# correos eliminar
def eliminar_correo(request, id):
    # correo = get_object_or_404(RegistrarUsuario, id=id)
    correo = RegistrarUsuario.objects.get(id=id)
    correo.delete()
    messages.info(request, "El correo" + " " + correo.correousu + " " + "fue eliminado")
    return redirect(to="listar_usuarios")
