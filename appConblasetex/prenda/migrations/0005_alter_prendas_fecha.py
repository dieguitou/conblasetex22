# Generated by Django 3.2.13 on 2022-09-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenda', '0004_alter_prendas_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prendas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='fecha de creacion'),
        ),
    ]