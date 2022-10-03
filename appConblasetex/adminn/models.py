from django.db import models


# Create your models here.
class RegistrarUsuario(models.Model):
    nombreUsu = models.CharField('nombre de usu', max_length=250)
    correousu = models.EmailField('correo usu')
    mensaje = models.CharField('mesajeusu', max_length=250)


class CorreosHistorial(models.Model):
    nombreArchi = models.CharField('nombre archivo', max_length=250)
    fechaArach = models.DateField('fecha de envio')
    id_registrousuario = models.ForeignKey(RegistrarUsuario, on_delete=models.CASCADE)
