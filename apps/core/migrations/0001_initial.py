# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoEmergencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('is_directo', models.BooleanField()),
                ('telefono_area', models.CharField(max_length=4)),
                ('telefono_numero', models.CharField(max_length=10)),
                ('sitio_web', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('direccion', models.CharField(max_length=50)),
                ('latitud', models.CharField(max_length=25)),
                ('longitud', models.CharField(max_length=25)),
                ('tipo_contacto', models.CharField(max_length=25)),
                ('is_valido', models.BooleanField()),
            ],
            options={
                'db_table': 'ContactoEmergencia',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('localidad', models.CharField(max_length=255, db_column=b'localidad')),
            ],
            options={
                'db_table': 'localidades',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provincia', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'provincias',
            },
        ),
        migrations.AddField(
            model_name='localidad',
            name='provincia',
            field=models.ForeignKey(to='core.Provincia', db_column=b'id_provincia'),
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='localidad',
            field=models.ForeignKey(to='core.Localidad'),
        ),
        migrations.AddField(
            model_name='contactoemergencia',
            name='provincia',
            field=models.ForeignKey(to='core.Provincia'),
        ),
    ]
