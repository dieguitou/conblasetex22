# Generated by Django 3.2.13 on 2022-07-27 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(verbose_name='cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Prendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='nombre de prenda')),
                ('tipoTela', models.CharField(max_length=250, verbose_name='tipo de tela')),
                ('color', models.CharField(max_length=250, verbose_name='Color')),
                ('talla', models.CharField(max_length=250, verbose_name='Talla')),
                ('caracteristica', models.CharField(max_length=250, verbose_name='caracteristica')),
                ('descripcion', models.CharField(max_length=250, verbose_name='descripcion de la prenda')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='precio')),
                ('imagen', models.ImageField(upload_to='fotos/', verbose_name='imagen de prenda')),
                ('fecha', models.DateTimeField(verbose_name='fecha de creacion')),
                ('idStock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prenda.stock')),
            ],
        ),
    ]
