
from django.forms import ModelForm
from django import forms
from .models import *
import datetime

class ContactoEmergenciaForm(forms.ModelForm):
    TIPO_CONTACTO_CHOICES = (
        ('1','POLICIALES'),
        ('2','MEDICAS'),
        ('3','CIVILES'),
        ('4','EN VIAJE'),
    )
    tipo_contacto       = forms.ChoiceField(widget=forms.Select(attrs=dict({'class':'form-control'})),choices = TIPO_CONTACTO_CHOICES)
    nombre              = forms.CharField(required=True,widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level','placeholder':'Nombre del contacto de Emergencia','required':'required'})))
    direccion           = forms.CharField(required=True,widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level','placeholder':'Calle','required':'required'})))
    localidad           = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control','required':'required'})), queryset = Localidad.objects.all(),empty_label = 'Seleccione una ciudad')
    provincia           = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control','required':'required'})), queryset = Provincia.objects.all(), empty_label = 'Seleccione un provincia')
    numero              = forms.CharField(widget = forms.TextInput(attrs = dict({'class':'form-control input-block-level solo-numero','placeholder':'Numero','required':'required'})),required=True)
    interseccion        = forms.CharField(required=False,widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level','placeholder':'Interseccion'})))
    latitud             = forms.CharField(widget=forms.HiddenInput())
    longitud            = forms.CharField(widget=forms.HiddenInput())
    is_directo          = forms.BooleanField(required=False)
    telefono_area       = forms.CharField(required=False,widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level','placeholder':'(0280)','display':'block'})))
    telefono_numero     = forms.CharField(required=False,widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level','placeholder':'ej:154123456'})))
    sitio_web           = forms.CharField(required=False,widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level','placeholder':'Ingrese la direccion del sitio web.'})))
    mail               = forms.CharField(required=False,widget=forms.EmailInput(attrs=dict({'class':'form-control input-block-level','placeholder':'Ingrese la direccion de correo electronico'})))

    class Meta:
        model = ContactoEmergencia
        exclude = ['is_valido','sugerido','sugiere']

class EditarContactoForm(forms.Form):
    """docstring for EditarContactoForm"""
    editar_provincia           = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control','required':'required'})), queryset = Provincia.objects.all(), empty_label = 'Seleccione un provincia')
    editar_localidad           = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control','required':'required'})), queryset = Localidad.objects.all(),empty_label = 'Seleccione una ciudad')
