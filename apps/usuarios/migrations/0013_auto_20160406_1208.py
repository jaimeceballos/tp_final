# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20160401_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoEmergencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono_area', models.CharField(max_length=4)),
                ('telefono_numero', models.CharField(max_length=10)),
                ('correo_electronico', models.EmailField(max_length=254, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='datos_medicos_interes',
            field=models.TextField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tipo_sangre',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 12, 8, 59, 685843)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contactos_emergencia',
            field=models.ManyToManyField(to='usuarios.ContactoEmergencia'),
        ),
    ]
