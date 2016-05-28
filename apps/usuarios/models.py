from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from datetime import datetime,date


class ContactoEmergenciaPersona(models.Model):
	nombre = models.CharField(max_length=50)
	telefono_area = models.CharField(max_length=4)
	telefono_numero= models.CharField(max_length=10)
	correo_electronico = models.EmailField(blank=True,null=True)

	class Meta:
		db_table = 'ContactoEmergenciaPersona'

class UserProfile(models.Model):
	user = models.OneToOneField(User,related_name='profile')
	mes_nac = models.IntegerField(null=True)
	dia_nac = models.IntegerField(null=True)
	anio_nac = models.IntegerField(null=True)
	activation_key = models.CharField(max_length=40, blank=True)
	key_expires = models.DateTimeField(default=datetime.today())
	avatar 	= models.ImageField(upload_to='apps/usuarios/avatar/',null=True,blank=True)
	tipo_sangre = models.CharField(max_length=10, null = True, blank = True)
	datos_medicos_interes = models.TextField(max_length=100, null = True, blank = True)
	contactos_emergencia = models.ManyToManyField(ContactoEmergenciaPersona)

	class Meta:
		db_table = 'UserProfile'

	def user_profile(sender, instance, signal, *args, **kwargs):
		profile, new = UserProfile.objects.get_or_create(user=instance)

	signals.post_save.connect(user_profile, sender=User)
