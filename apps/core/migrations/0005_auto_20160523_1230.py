# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160520_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datoscontacto',
            name='contacto',
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='is_directo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='sitio_web',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='telefono_area',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='telefono_numero',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='DatosContacto',
        ),
    ]
