from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from datetime import datetime,date

class Provincia(models.Model):
    provincia = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.provincia

    class Meta:
        db_table = 'provincias'

class Localidad(models.Model):
    provincia = models.ForeignKey('Provincia',db_column = 'id_provincia')
    localidad = models.CharField(max_length=255,db_column = 'localidad')

    def __unicode__(self):
        return u'%s' % self.localidad

    class Meta:
        db_table = 'localidades'

class ContactoEmergencia(models.Model):
    nombre              = models.CharField(max_length=50)
    direccion           = models.CharField(max_length=50)
    numero              = models.CharField(max_length=4)
    interseccion        = models.CharField(max_length=50,null=True,blank=True)
    latitud             = models.CharField(max_length=25)
    longitud            = models.CharField(max_length=25)
    tipo_contacto       = models.CharField(max_length=25)
    provincia           = models.ForeignKey('Provincia')
    localidad           = models.ForeignKey('Localidad')
    is_valido           = models.BooleanField(default=False)
    is_directo          = models.BooleanField(default=False)
    telefono_area       = models.CharField(max_length=4,null=True,blank=True)
    telefono_numero     = models.CharField(max_length=10,null=True,blank=True)
    sitio_web           = models.CharField(max_length=50,null=True,blank=True)
    mail                = models.EmailField(null=True,blank=True)

    class Meta:
        db_table = 'ContactoEmergencia'
        unique_together = ("nombre","localidad")
