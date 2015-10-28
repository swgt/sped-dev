# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spedread', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloco',
            name='nome',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='campo',
            name='nome',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='registro',
            name='nome',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
