from django.forms import *
from appConblasetex.prenda.models import *
from django import forms

BIRTH_YEAR_CHOICES = ['2000', '2001', '2002']


# forms chaleco
class PrendaForms(ModelForm):
    class Meta:
        model = Prendas
        # fields = '__all__'

        fields = ['nombre', 'tipoTela', 'color', 'imagen', 'precio', 'fecha']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nombre',
                    'name': 'txtnombre',
                }
            ),
            'tipoTela': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'tipoTela',
                }
            ),
            'color': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'color',
                }
            ),
            'imagen': FileInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'precio': NumberInput(
                attrs={
                    'placeholder': 'precio',
                    'class': 'form-control',

                }
            ),
            'fecha': forms.SelectDateWidget(
                attrs={

                }
            ),

        }


class PrendaFormsv1(ModelForm):
    class Meta:
        model = Prendas
        # fields = '__all__'

        fields = ['nombre', 'color', 'imagen', 'precio', 'fecha']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nombre',
                    'name': 'txtnombre',
                }
            ),
            'color': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'color',
                }
            ),
            'imagen': FileInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'precio': NumberInput(
                attrs={
                    'placeholder': 'precio',
                    'class': 'form-control',

                }
            ),
            'fecha': forms.SelectDateWidget(
                attrs={

                }
            ),

        }


# para editar productos epp
class PrendaEppForms(ModelForm):
    class Meta:
        model = Producto
        # fields = '__all__'

        fields = ['nombre', 'tipo']
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nombre',
                }
            ),
            'tipo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'tipo',
                }
            ),
        }


# login
# modelo template viste
# patrones de diseno
# entvi Modelo Vista Template


class FormDetalle(ModelForm):
    class Meta:
        model = Prendas
        # fields = '__all__'

        fields = ['tipoTela', 'color', 'imagen', 'precio']
        widgets = {
            'tipoTela': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'tipoTela',
                    'disabled': 'True',
                }
            ),
            'color': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'color',
                    'disabled': 'True',
                }
            ),
            'imagen': FileInput(
                attrs={
                    'class': 'form-control',

                }
            ),
            'precio': NumberInput(
                attrs={
                    'placeholder': 'precio',
                    'class': 'form-control',
                    'disabled': 'True',

                }
            ),

        }
