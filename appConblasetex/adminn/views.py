from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from .models import RegistrarUsuario

import smtplib
from email.mime.text import MIMEText

from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views.generic import *
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
class IndexA(TemplateView):
    template_name = 'temp2/indexadmin.html'


class RegistrarUsu(View):
    @staticmethod
    def post(request):
        nombre = request.POST['txtNombreusu']
        corre = request.POST['txtcorreo']
        mensaje = request.POST['txtmensaje']
        RegistrarUsuario.objects.create(nombreUsu=nombre, correousu=corre, mensaje=mensaje)
        return redirect('cont')


class ListarUsu(TemplateView):
    template_name = 'temp2/enviarCatalogo.html'

    def get_context_data(self, **kwargs):
        usuarios3 = RegistrarUsuario.objects.all()
        correos = RegistrarUsuario.objects.all().values('correousu')
        for c in correos:
            print(c)
        return {'usuarios3': usuarios3, 'correos': correos}


class mandarCorreo_(View):
    def post(self, request):
        try:
            correos = RegistrarUsuario.objects.all()
            a = 'diegoinmortal2@gmail.com,eugenia1gorostiaga@gmail.com,dgorostiagam@fcpn.edu.bo,miquimao047@gmail.com'
            lista = []
            lista = (a.split(','))
            mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            print(mailServer.ehlo())
            mailServer.starttls()
            print(mailServer.ehlo())
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            print('Conectado....')
            for r in correos:
                mensaje = MIMEText("""Hola miguel desde la terminal de Buses La Paz""")
                mensaje['From'] = settings.EMAIL_HOST_USER
                print(r.correousu)
                mensaje['To'] = str(r.correousu)
                mensaje['Subject'] = "Tienes un correo"
                mailServer.sendmail(settings.EMAIL_HOST_USER,
                                    str(r.correousu),
                                    mensaje.as_string())
                print('correo enviado')

        except Exception as e:
            print('error')
            print(e)

        return redirect('listar_usuarios')
