from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse,HttpResponseRedirect, HttpResponse,Http404
from django.core.urlresolvers import reverse
from django.db import transaction,IntegrityError
import time
from datetime import timedelta,date
from django.core import serializers
# Create your views here.

def contacto_emergencia(request):
    form = ContactoEmergenciaForm()
    contacto = ContactoEmergencia()
    values = {
        'form' : form,
        'contacto' : contacto,
    }

    return render_to_response('core/test.html',values,context_instance=RequestContext(request))

def save_contacto(request):
    form            = ContactoEmergenciaForm()
    contacto        = ContactoEmergencia()
    values = {
        'form' : form,
        'contacto' : contacto,
        'msg' : 'Por favor revise el formulario.'
    }
    if request.method == 'POST':
        form = ContactoEmergenciaForm(request.POST)
        print form.errors
        if form.is_valid():
            contacto.nombre         = form.cleaned_data['nombre'].upper()
            contacto.direccion      = form.cleaned_data['direccion'].upper()
            contacto.tipo_contacto  = form.cleaned_data['tipo_contacto']
            contacto.provincia      = form.cleaned_data['provincia']
            contacto.localidad      = form.cleaned_data['localidad']
            contacto.latitud        = form.cleaned_data['latitud']
            contacto.longitud       = form.cleaned_data['longitud']
            contacto.is_valido      = True
            contacto.numero         = form.cleaned_data['numero']
            contacto.interseccion    = form.cleaned_data['interseccion'].upper()
            contacto.is_directo        = form.cleaned_data['is_directo']
            contacto.telefono_area     = form.cleaned_data['telefono_area']
            contacto.telefono_numero   = form.cleaned_data['telefono_numero']
            contacto.sitio_web         = form.cleaned_data['sitio_web']
            contacto.mail              = form.cleaned_data['mail']

            try:
                contacto.save()
                values['msg']           = 'Guardado con exito'
                values['form']          = ContactoEmergenciaForm()
                values['contacto']      = ContactoEmergencia()
            except IntegrityError as e:
                if "UNIQUE constraint failed" in e.message:
                    values['msg']       = 'El contacto que intenta cargar ya existe.'
    return render_to_response('core/test.html',values,context_instance=RequestContext(request))

def obtener_ciudades(request,provincia):
    data        = request.POST
    ciudades    = Localidad.objects.filter(provincia = provincia)
    data        = serializers.serialize("json",ciudades)
    return HttpResponse(data, content_type = 'application/json')
