# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0023_auto_20150807_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penaltylog',
            name='type',
            field=models.PositiveSmallIntegerField(verbose_name='typ kary', choices=[(1, 'kick'), (2, 'admin jail'), (3, 'warn'), (4, 'ban'), (5, 'blokada postaci')]),
        ),
    ]
