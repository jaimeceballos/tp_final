# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosContacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_directo', models.BooleanField()),
                ('telefono_area', models.CharField(max_length=4)),
                ('telefono_numero', models.CharField(max_length=10)),
                ('sitio_web', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254, null=True)),
            ],
            options={
                'db_table': 'DatosContacto',
            },
        ),
        migrations.AlterUniqueTogether(
            name='contactoemergencia',
            unique_together=set([('nombre', 'localidad')]),
        ),
        migrations.RemoveField(
            model_name='contactoemergencia',
            name='is_directo',
        ),
        migrations.RemoveField(
            model_name='contactoemergencia',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='contactoemergencia',
            name='sitio_web',
        ),
        migrations.RemoveField(
            model_name='contactoemergencia',
            name='telefono_area',
        ),
        migrations.RemoveField(
            model_name='contactoemergencia',
            name='telefono_numero',
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='contacto',
            field=models.ManyToManyField(to='core.DatosContacto'),
        ),
    ]
