# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20151217_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='anio_nac',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dia_nac',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 17, 11, 53, 5, 193740), null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mes_nac',
            field=models.IntegerField(null=True),
        ),
    ]
