# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160523_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactoemergencia',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
