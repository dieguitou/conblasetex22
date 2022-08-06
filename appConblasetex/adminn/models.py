from django.db import models


# Create your models here.
class RegistrarUsuario(models.Model):
    nombreUsu = models.CharField('nombre de usu', max_length=250)
    correousu = models.EmailField('correo usu')
    mensaje = models.CharField('mesajeusu', max_length=250)
