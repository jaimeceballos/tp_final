from django.conf.urls import include, url
from .views import *

urlpatterns = [
   #url(r'^$', auth_views.login, {'template_name': 'login.html'},name='login'),
   url(r'^contacto/$',contacto_emergencia,name='contacto'),
   url(r'^contacto_save/$',save_contacto,name='contacto_save'),
   url(r'^obtenerciudades/(?P<provincia>[0-9A-Za-z]+)/$', obtener_ciudades, name = 'obtener_ciudades'),
]
