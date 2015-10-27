# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spedread', '0002_auto_20151022_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
