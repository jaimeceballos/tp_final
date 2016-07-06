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
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import json
# Create your views here.

@login_required(login_url='login')
def contacto_emergencia(request):
    form = ContactoEmergenciaForm()
    contacto = ContactoEmergencia()
    values = {
        'form' : form,
        'contacto' : contacto,
    }

    return render_to_response('core/test.html',values,context_instance=RequestContext(request))

@login_required(login_url='login')
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
        if form.is_valid():
            contacto_prepared_save(request,contacto,form,False,values)
    return render_to_response('core/test.html',values,context_instance=RequestContext(request))

@login_required(login_url='login')
def obtener_ciudades(request,provincia):
    ciudades    = Localidad.objects.filter(provincia = provincia)
    data        = serializers.serialize("json",ciudades)
    return HttpResponse(data, content_type = 'application/json')

@login_required(login_url='login')
def obtener_contactos(request,provincia,localidad):
    provincia = Provincia.objects.get(provincia__icontains = provincia)
    localidad = Localidad.objects.get(provincia = provincia.id, localidad__icontains = localidad)
    contactos = ContactoEmergencia.objects.filter(provincia = provincia,localidad = localidad,is_valido=True)
    data = serializers.serialize("json",contactos)
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='login')
def ver_contactos(request):

    return render_to_response('core/ver_contactos.html',{},context_instance=RequestContext(request))

@login_required(login_url='login')
def compartir_contacto(request):
    form = ContactoEmergenciaForm()
    contacto = ContactoEmergencia()
    values = {
        'form' : form,
        'contacto' : contacto,
    }
    if request.method == 'POST':
        form = ContactoEmergenciaForm(request.POST)
        if form.is_valid():
            if contacto_prepared_save(request,contacto,form,True,values):
                values["msg"] = "Gracias por colaborar, tu aporte esta siendo analizado y verificado por un administrador."
            else:
                values["msg"] = "Ocurrio un error, Verifica que el contacto no exista y volve a intentarlo mas tarde, gracias!"
    return render_to_response('core/compartir_contacto.html',values,context_instance=RequestContext(request))


def contacto_prepared_save(request,contacto,form,sugerido,values):
    contacto.nombre         = form.cleaned_data['nombre'].upper()
    contacto.direccion      = form.cleaned_data['direccion'].upper()
    contacto.tipo_contacto  = form.cleaned_data['tipo_contacto']
    contacto.provincia      = form.cleaned_data['provincia']
    contacto.localidad      = form.cleaned_data['localidad']
    contacto.latitud        = form.cleaned_data['latitud']
    contacto.longitud       = form.cleaned_data['longitud']
    contacto.is_valido      = not sugerido
    contacto.numero         = form.cleaned_data['numero']
    contacto.interseccion    = form.cleaned_data['interseccion'].upper()
    contacto.is_directo        = form.cleaned_data['is_directo']
    contacto.telefono_area     = form.cleaned_data['telefono_area']
    contacto.telefono_numero   = form.cleaned_data['telefono_numero']
    contacto.sitio_web         = form.cleaned_data['sitio_web']
    contacto.mail              = form.cleaned_data['mail']
    contacto.sugerido          = sugerido
    if sugerido:
        contacto.sugiere = request.user
    try:
        contacto.save()
        values['msg']           = 'Guardado con exito'
        values['form']          = ContactoEmergenciaForm()
        values['contacto']      = ContactoEmergencia()
        return 1
    except IntegrityError as e:
        if "UNIQUE constraint failed" in e.message:
            values['msg']       = 'El contacto que intenta cargar ya existe.'
        return 0

@login_required(login_url='login')
@staff_member_required
def verificar_sugeridos(request):
    sugeridos = ContactoEmergencia.objects.filter(is_valido = False).count()
    data = json.dumps(sugeridos)
    return HttpResponse(data)

@login_required(login_url='login')
@staff_member_required
def sugeridos(request):
    values = {}
    sugeridos = ContactoEmergencia.objects.filter(is_valido = False, sugerido = True)
    values['sugeridos'] = sugeridos
    return render_to_response("core/sugeridos.html",values,context_instance=RequestContext(request))

@login_required(login_url='login')
@staff_member_required
def sugerido(request,id):
    sugerido = ContactoEmergencia.objects.get(id=id)
    data = serializers.serialize("json",[sugerido,])
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='login')
@staff_member_required
def validar(request,id):
    contacto = ContactoEmergencia.objects.get(id=id)
    contacto.is_valido = True
    contacto.save()
    return HttpResponse("Se valido el contacto.")

@login_required(login_url='login')
@staff_member_required
def editar(request,id):
    form        = ContactoEmergenciaForm(instance = ContactoEmergencia.objects.get(id=id))
    contacto    = ContactoEmergencia.objects.get(id=id)
    retorno = 'sugeridos'
    try:
        retorno     = request.session.get('retorno')
        del(request.session['retorno'])
    except:
        retorno = 'sugeridos'

    values = {
        'form' : form,
        'contacto' : contacto,
    }
    if request.method == 'POST':
        form = ContactoEmergenciaForm(request.POST)
        print form.is_valid()
        if form.is_valid():
            contacto.nombre         = form.cleaned_data['nombre'].upper()
            contacto.direccion      = form.cleaned_data['direccion'].upper()
            contacto.tipo_contacto  = form.cleaned_data['tipo_contacto']
            contacto.provincia      = form.cleaned_data['provincia']
            contacto.localidad      = form.cleaned_data['localidad']
            contacto.latitud        = form.cleaned_data['latitud']
            contacto.longitud       = form.cleaned_data['longitud']
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
                return HttpResponseRedirect(reverse(retorno))
            except IntegrityError as e:
                print e
                pass
    sugeridos = ContactoEmergencia.objects.filter(is_valido = False, sugerido = True)
    values['sugeridos'] = sugeridos
    return render_to_response("core/editar.html",values,context_instance=RequestContext(request))

@login_required(login_url='login')
@staff_member_required
def editar_contacto(request):
    form = EditarContactoForm()
    values = {
        'form' : form,
    }
    return render_to_response('core/editar_contacto.html',values,context_instance=RequestContext(request))

@login_required(login_url='login')
@staff_member_required
def cantidad_en_provincia(request,provincia):
    contactos = ContactoEmergencia.objects.filter(provincia=provincia).count()
    data = json.dumps(contactos)
    return HttpResponse(data)

@login_required(login_url='login')
@staff_member_required
def cantidad_en_ciudad(request,ciudad):
    contactos = ContactoEmergencia.objects.filter(localidad=ciudad).count()
    data = json.dumps(contactos)
    return HttpResponse(data)

@login_required(login_url='login')
@staff_member_required
def contactos_provincia(request,provincia):
    contactos = ContactoEmergencia.objects.filter(provincia = provincia)
    data = serializers.serialize("json",contactos)
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='login')
@staff_member_required
def contactos_ciudad(request,ciudad):
    contactos = ContactoEmergencia.objects.filter(localidad = ciudad)
    data = serializers.serialize("json",contactos)
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='login')
@staff_member_required
def obtener_localidad(request,ciudad):
    localidad = Localidad.objects.get(id=ciudad)
    data = serializers.serialize("json",[localidad,])
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='login')
@staff_member_required
def editar_contacto_id(request,id):
    contacto = ContactoEmergencia.objects.get(id=id)
    form = ContactoEmergenciaForm(instance = contacto)
    request.session['retorno'] = 'editar_contacto'
    values = {
        'contacto' : contacto,
        'form' : form,
        }
    return render_to_response("core/edicion_contacto.html",values,context_instance=RequestContext(request))
