from django.conf.urls import include, url
from .views import *

urlpatterns = [
   #url(r'^$', auth_views.login, {'template_name': 'login.html'},name='login'),
   url(r'^contacto/$',contacto_emergencia,name='contacto'),
   url(r'^contacto_save/$',save_contacto,name='contacto_save'),
   url(r'^obtenerciudades/(?P<provincia>[0-9A-Za-z]+)/$', obtener_ciudades, name = 'obtener_ciudades'),
   url(r'^ver_contactos/$',ver_contactos, name='ver_contactos'),
   url(r'^obtenercontactos/(?P<provincia>[0-9A-Za-z]+)/(?P<localidad>[0-9A-Za-z]+)/$', obtener_contactos, name = 'obtener_contactos'),
   url(r'^compartir_contacto/$',compartir_contacto,name='compartir_contacto'),
   url(r'^verificar_sugeridos/$',verificar_sugeridos,name='verificar_sugeridos'),
   url(r'^sugeridos/$',sugeridos,name='sugeridos'),
   url(r'^sugerido/(?P<id>[0-9A-Za-z]+)/$',sugerido,name='sugerido'),
   url(r'^validar/(?P<id>[0-9A-Za-z]+)/$',validar,name='validar'),
   url(r'^editar/(?P<id>[0-9A-Za-z]+)/$',editar,name='editar'),
   url(r'^editar_contacto/$',editar_contacto,name='editar_contacto'),
   url(r'^editar_contacto/(?P<id>[0-9A-Za-z]+)/$',editar_contacto_id,name='editar_contacto_id'),
   url(r'^cantidad_en_provincia/(?P<provincia>[0-9A-Za-z]+)/$',cantidad_en_provincia,name='cantidad_en_provincia'),
   url(r'^cantidad_en_ciudad/(?P<ciudad>[0-9A-Za-z]+)/$',cantidad_en_ciudad,name='cantidad_en_ciudad'),
   url(r'^contactos_provincia/(?P<provincia>[0-9A-Za-z]+)/$',contactos_provincia,name='contactos_provincia'),
   url(r'^contactos_ciudad/(?P<ciudad>[0-9A-Za-z]+)/$',contactos_ciudad,name='contactos_ciudad'),
   url(r'^obtener_localidad/(?P<ciudad>[0-9A-Za-z]+)/$',obtener_localidad,name='obtener_localidad'),
]
