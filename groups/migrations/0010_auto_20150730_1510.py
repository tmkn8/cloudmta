# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0009_auto_20150718_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupinvitation',
            name='date',
            field=models.DateTimeField(verbose_name='Data zaproszenia', auto_now_add=True),
        ),
    ]
