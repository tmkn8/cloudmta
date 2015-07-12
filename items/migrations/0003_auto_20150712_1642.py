# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20150712_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='rx',
            field=models.FloatField(default=0, verbose_name='Rotacja X'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ry',
            field=models.FloatField(default=0, verbose_name='Rotacja Y'),
        ),
        migrations.AlterField(
            model_name='item',
            name='rz',
            field=models.FloatField(default=0, verbose_name='Rotacja Z'),
        ),
    ]
