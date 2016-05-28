# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160520_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactoemergencia',
            name='numero',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='datoscontacto',
            name='contacto',
            field=models.ForeignKey(to='core.ContactoEmergencia'),
        ),
    ]
