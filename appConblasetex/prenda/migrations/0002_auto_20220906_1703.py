# Generated by Django 3.2.13 on 2022-09-06 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prenda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prendas',
            name='tipo',
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.CharField(default='', max_length=250, verbose_name='tipo del producto'),
        ),
    ]