from django.db import models
from appConblasetex.epp.models import Epp
from appConblasetex.prenda.models import Prendas


# Create your models here.
class Venta(models.Model):
    fechaVenta = models.DateField('fecha de venta')
    ConstoTotal = models.PositiveIntegerField('contoTotal')


class VentaUnidadP(models.Model):
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    idPrenda = models.ForeignKey(Prendas, on_delete=models.CASCADE)
    cantida = models.PositiveIntegerField('cantidadVuP')
    costo = models.PositiveIntegerField('contoVuP')


class VentaUnidadE(models.Model):
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    idEpp = models.ForeignKey(Epp, on_delete=models.CASCADE)
    cantida = models.PositiveIntegerField('cantidadVuE')
    costo = models.PositiveIntegerField('contoVuE')
