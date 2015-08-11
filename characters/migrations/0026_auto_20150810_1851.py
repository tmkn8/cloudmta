# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0025_auto_20150810_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penaltylog',
            name='expire',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='data wygaśnięcia'),
        ),
        migrations.AlterField(
            model_name='penaltylog',
            name='time',
            field=models.PositiveIntegerField(verbose_name='data nadania'),
        ),
    ]
