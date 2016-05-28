# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0023_auto_20160523_1652'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactoEmergencia',
            new_name='ContactoEmergenciaPersona',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 27, 20, 22, 39, 801048)),
        ),
        migrations.AlterModelTable(
            name='contactoemergenciapersona',
            table='ContactoEmergenciaPersona',
        ),
    ]
