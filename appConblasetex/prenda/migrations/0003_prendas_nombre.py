# Generated by Django 3.2.13 on 2022-09-07 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenda', '0002_auto_20220906_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='prendas',
            name='nombre',
            field=models.CharField(default='', max_length=250, verbose_name='nombre'),
        ),
    ]
