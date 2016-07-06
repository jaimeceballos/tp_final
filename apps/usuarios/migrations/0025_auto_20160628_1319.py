# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import apps.usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0024_auto_20160527_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=apps.usuarios.models.get_image_path, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 28, 13, 19, 16, 560643)),
        ),
    ]
