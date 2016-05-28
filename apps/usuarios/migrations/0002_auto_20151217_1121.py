# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='primer_logueo',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='anio_nac',
            field=models.IntegerField(default=2015),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 11, 21, 12, 182003)),
        ),
    ]
