from django.db import models


class Stock(models.Model):
    cantidad = models.PositiveIntegerField('cantidad')


class Prendas(models.Model):
    nombre = models.CharField('nombre de prenda', max_length=250)
    tipoTela = models.CharField('tipo de tela', max_length=250)
    color = models.CharField('Color', max_length=250)
    talla = models.CharField('Talla', max_length=250)
    caracteristica = models.CharField('caracteristica', max_length=250)
    descripcion = models.CharField('descripcion de la prenda', max_length=250)
    precio = models.DecimalField('precio', max_digits=10, decimal_places=2)
    imagen = models.ImageField('imagen de prenda', upload_to='fotos/')
    fecha = models.DateTimeField('fecha de creacion')
    idStock = models.ForeignKey(Stock, on_delete=models.CASCADE)
