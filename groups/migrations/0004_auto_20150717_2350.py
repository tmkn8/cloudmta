# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20150713_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='userid',
            field=models.ForeignKey(related_query_name='groupsmember', db_column='userID', to='characters.Character', related_name='groupmembers', verbose_name='Postać'),
        ),
    ]
