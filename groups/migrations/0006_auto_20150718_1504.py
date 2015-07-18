# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20150717_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='rankid',
            field=models.ForeignKey(db_column='rankID', verbose_name='Ranga', related_name='groupmembers', to='groups.GroupRank', related_query_name='groupmember'),
        ),
    ]
