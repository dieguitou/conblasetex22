# Generated by Django 3.2.13 on 2022-07-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrarUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsu', models.CharField(max_length=250, verbose_name='nombre de usu')),
                ('correousu', models.EmailField(max_length=254, verbose_name='correo usu')),
                ('mensaje', models.CharField(max_length=250, verbose_name='mesajeusu')),
            ],
        ),
    ]