# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20160523_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactoemergencia',
            name='sugerido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='sugiere',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
