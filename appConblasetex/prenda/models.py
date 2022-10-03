from django.db import models


class Producto(models.Model):
    nombre = models.CharField('nombre producto', max_length=250)
    tipo = models.CharField('tipo del producto', default='', max_length=250)

    def __str__(self):
        return self.nombre


class Prendas(models.Model):
    nombre = models.CharField('nombre', max_length=250, default='')
    tipoTela = models.CharField('tipo de tela', max_length=250)
    color = models.CharField('Color', max_length=250)
    talla = models.CharField('Talla', max_length=250)
    descripcion = models.CharField('descripcion de la prenda', max_length=250)
    precio = models.DecimalField('precio', max_digits=10, decimal_places=2)
    imagen = models.ImageField('imagen de prenda', upload_to='fotos/')
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField('fecha de creacion', default=None, null=True, blank=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
