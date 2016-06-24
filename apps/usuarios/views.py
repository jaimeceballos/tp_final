#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response,get_object_or_404
from django.template import Context, Template, RequestContext
from .models import *
from .forms import *
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
import hashlib,random
from django.utils import timezone
from datetime import datetime,time,timedelta
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

# Create your views here.

def registro(request):
	form = RegistroForm()
	values = {
		'form':form,
	}
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			user = User()
			try:
				if request.session.get('contributor',True):
					user.is_staff  = True
					password = form.cleaned_data['password']
			except:
				user.is_staff = False
			user.username = form.cleaned_data['email']
			user.first_name = form.cleaned_data['nombre']
			user.last_name = form.cleaned_data['apellido']
			user.email 	= form.cleaned_data['email']
			user.set_password(form.cleaned_data['password'])
			user.is_active = False
			user.save()
			salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
			activation_key = hashlib.sha1(salt+user.email).hexdigest()
			key_expires = datetime.today() + timedelta(2)
			profile = user.profile
			profile.dia_nac = form.cleaned_data['dia_nacimiento']
			profile.mes_nac = form.cleaned_data['mes_nacimiento']
			profile.anio_nac = form.cleaned_data['anio_nacimiento']
			profile.activation_key = activation_key
			profile.key_expires = key_expires
			profile.save()
			subject, from_email, to = 'Confirmacion de cuenta','jaimeceballos82@gmail.com',user.username
			text_content = 'Hola %s: ' % user.first_name
			if user.is_staff:
				html_content = '<strong>Hola %s:</strong><br>Recibiste este e-mail porque recientemente has sido dado de alta como colaborador en nuestro sitio.<br> Tu usuario es: %s y tu contrase&ntilde;a: %s <br>Hace click en el siguiente link para confirmar tu registro <br> <a href="http://127.0.0.1:8000/usuarios/confirmar/%s/" target="_blank">http://127.0.0.1:8000/usuarios/confirmar/%s/</a> <br> Record&aacute; que este link es valido solo por 48 horas. <br> Muchas gracias.' % (user.first_name,user.username,password,activation_key,activation_key)
			else:
				html_content = '<strong>Hola %s:</strong><br>Recibiste este e-mail porque recientemente te has registrado en nuestro sitio.<br> Hace click en el siguiente link para confirmar tu registro <br> <a href="http://127.0.0.1:8000/usuarios/confirmar/%s/" target="_blank">http://127.0.0.1:8000/usuarios/confirmar/%s/</a> <br> Record&aacute; que este link es valido solo por 48 horas. <br>Si no realizaste ninguna solicitud de registro, te pedimos disculpas y desestima el presente correo.<br> Muchas gracias.' % (user.first_name,activation_key,activation_key)
			msg = EmailMultiAlternatives(subject,text_content,from_email,[to])
			msg.attach_alternative(html_content,"text/html")
			msg.send()
			#send_mail(email_subject,email_body,'jaimeceballos82@gmail.com',[user.username],fail_silently=False)
			if request.user.is_authenticated():
				return HttpResponseRedirect(reverse('home'))
			return render_to_response('registro_confirm.html',values,context_instance=RequestContext(request))


	return render_to_response('registro.html',values,context_instance=RequestContext(request))

def confirmar(request,activation_key):
	# Verifica que el usuario ya está logeado
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))

    # Verifica que el token de activación sea válido y sino retorna un 404
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    # verifica si el token de activación ha expirado y si es así renderiza el html de registro expirado
    if user_profile.key_expires < timezone.now():
    	user = user_profile.user
    	if user.is_active:
    		return render_to_response('link_usado.html',{},context_instance=RequestContext(request))
    	user_profile.delete()
    	user.delete()
        return render_to_response('confirmacion_vencida.html')
    # Si el token no ha expirado, se activa el usuario y se muestra el html de confirmación
    user = user_profile.user
    if user.is_active:
    	return render_to_response('link_usado.html',{},context_instance=RequestContext(request))
    user.is_active = True
    user.save()
    return render_to_response('usuario_activado.html')

def logout(request):
    auth.logout(request)

    return HttpResponseRedirect(reverse('home'))

@login_required(login_url='login')
def editar_perfil(request):
	usuario = request.user
	profile = usuario.profile
	userForm = UserForm(instance=usuario)
	profileForm = ProfileForm(instance=profile)
	personaContactoForm = ContactoEmergenciaPersonaForm()
	values = {
		'userForm' : userForm,
		'profileForm' :profileForm,
		'usuario' : usuario,
		'profile' : profile,
		'personaContactoForm':personaContactoForm,
 	}
	if request.method == 'POST':
		userForm = UserForm(request.POST)
		profileForm = ProfileForm(request.POST, request.FILES)
		print userForm.is_valid() or profileForm.is_valid()
		if userForm.is_valid() or profileForm.is_valid():
			usuario.first_name = userForm.data['first_name']
			usuario.last_name = userForm.data['last_name']
			usuario.email = userForm.data['email']
			profile.dia_nac = profileForm.data['dia_nac']
			profile.mes_nac = profileForm.data['mes_nac']
			profile.anio_nac = profileForm.data['anio_nac']
			try:
				profile.avatar = request.FILES['avatar']
			except Exception as e:
				profile.avatar = profile.avatar

			profile.tipo_sangre = profileForm.data['tipo_sangre']
			profile.datos_medicos_interes = profileForm.data['datos_medicos_interes']
			usuario.save()
			profile.save()
			usuario = request.user
			profile = usuario.profile
			userForm = UserForm(instance=usuario)
			profileForm = ProfileForm(instance=profile)
	values['contactosPersona'] = profile.contactos_emergencia.all().count()
	return render_to_response('usuarios/profile_edit.html',values,context_instance=RequestContext(request))

@login_required(login_url='login')
def cargar_contacto(request):
	if request.method == 'POST':
		profile = request.user.profile
		form = ContactoEmergenciaPersonaForm(request.POST)
		if form.is_valid():
			contacto = ContactoEmergenciaPersona()
			contacto.nombre = form.cleaned_data['nombre']
			contacto.telefono_area = form.cleaned_data['telefono_area']
			contacto.telefono_numero = form.cleaned_data['telefono_numero']
			contacto.correo_electronico = form.cleaned_data['correo_electronico']
			contacto.save()
			profile.contactos_emergencia.add(contacto)
	return HttpResponseRedirect(reverse('editar_perfil'))

def cargar_colaborador(request):
	registro = RegistroForm()
	request.session['contributor'] = True
	return render_to_response('usuarios/contributor.html',{'form':registro},context_instance=RequestContext(request))

@login_required(login_url='login')
def cambiar_password(request):
	form = CambiarPasswordForm()
	values = {
		'form':form,
	}
	if request.method == 'POST':
		form = CambiarPasswordForm(request.POST, request=request)
		values['form'] = form
		if form.is_valid():
			password = form.cleaned_data["nueva"]
			usuario = request.user
			username = usuario.username
			usuario.set_password(password)
			usuario.save()
			user = authenticate(username=username, password=password)
			login(request, user)
			values['message'] = 'Su contraseña ha sido cambiada con exito.'
	return render_to_response('cambiar_password.html',values,context_instance=RequestContext(request))
