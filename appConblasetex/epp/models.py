from django.db import models

from appConblasetex.prenda.models import Producto


# Create your models here.
class Epp(models.Model):
    nombreEpp = models.CharField('modebre epp', max_length=250)
    tipoEpp = models.CharField('tipo epp', max_length=250)
    tallaEpp = models.CharField('talla de epp', max_length=50)
    precioEpp = models.DecimalField('precio del epp', max_digits=10, decimal_places=2)
    fotoEpp = models.ImageField('imagen de epp', upload_to='fotosEpp/')
    fechaEpp = models.DateTimeField('fecha de creacion Epp')
    cantidad = models.PositiveIntegerField()
