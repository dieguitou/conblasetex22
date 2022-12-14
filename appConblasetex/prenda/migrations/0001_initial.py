# Generated by Django 3.2.13 on 2022-09-06 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='nombre producto')),
            ],
        ),
        migrations.CreateModel(
            name='Prendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=250, verbose_name='tipo del producto')),
                ('tipoTela', models.CharField(max_length=250, verbose_name='tipo de tela')),
                ('color', models.CharField(max_length=250, verbose_name='Color')),
                ('talla', models.CharField(max_length=250, verbose_name='Talla')),
                ('descripcion', models.CharField(max_length=250, verbose_name='descripcion de la prenda')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='precio')),
                ('imagen', models.ImageField(upload_to='fotos/', verbose_name='imagen de prenda')),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(verbose_name='fecha de creacion')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prenda.producto')),
            ],
        ),
    ]
