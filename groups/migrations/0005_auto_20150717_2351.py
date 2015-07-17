# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20150717_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='userid',
            field=models.ForeignKey(verbose_name='Postać', related_query_name='groupmember', db_column='userID', to='characters.Character', related_name='groupmembers'),
        ),
    ]
