# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('num_posicao', models.IntegerField()),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('bloco', models.ForeignKey(to='spedread.Bloco')),
            ],
        ),
        migrations.CreateModel(
            name='Sped',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('data_upload', models.DateField()),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ValoresSped',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('valor', models.CharField(max_length=255)),
                ('fim_linha', models.BooleanField()),
                ('campo', models.ForeignKey(to='spedread.Campo')),
                ('sped', models.ForeignKey(to='spedread.Sped')),
            ],
        ),
        migrations.AddField(
            model_name='campo',
            name='registro',
            field=models.ForeignKey(to='spedread.Registro'),
        ),
    ]
