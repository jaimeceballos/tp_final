# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160523_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactoemergencia',
            name='is_valido',
            field=models.BooleanField(default=False),
        ),
    ]
