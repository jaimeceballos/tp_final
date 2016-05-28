# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160406_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactoemergencia',
            name='contacto',
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='interseccion',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='numero',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='datoscontacto',
            name='contacto',
            field=models.ForeignKey(default=1, to='core.ContactoEmergencia'),
        ),
    ]
