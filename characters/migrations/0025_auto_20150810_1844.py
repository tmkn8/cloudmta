# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0024_auto_20150810_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penaltylog',
            name='type',
        ),
        migrations.AddField(
            model_name='penaltylog',
            name='penalty_type',
            field=models.PositiveSmallIntegerField(default=1, db_column='type', verbose_name='typ kary', choices=[(1, 'kick'), (2, 'admin jail'), (3, 'warn'), (4, 'ban'), (5, 'blokada postaci')]),
            preserve_default=False,
        ),
    ]
