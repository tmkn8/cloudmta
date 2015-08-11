# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0022_auto_20150807_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penaltylog',
            name='character',
            field=models.ForeignKey(db_column='userID', verbose_name='postać', related_query_name='character', to='characters.Character', related_name='characters'),
        ),
    ]
