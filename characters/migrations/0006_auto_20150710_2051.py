# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_auto_20150710_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='ingame',
            field=models.BooleanField(default=False, verbose_name='Postać w grze', db_column='inGame'),
        ),
    ]
