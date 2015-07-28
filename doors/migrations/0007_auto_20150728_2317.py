# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0006_threedtext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='shopid',
            field=models.ForeignKey(to='doors.Door', verbose_name='drzwi', related_name='clothes', db_column='shopID'),
        ),
        migrations.AlterField(
            model_name='doorpickup',
            name='parentid',
            field=models.ForeignKey(to='doors.Door', related_query_name='doorpickup', verbose_name='drzwi', related_name='doorpickups', db_column='parentID'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shopid',
            field=models.ForeignKey(to='doors.Door', verbose_name='drzwi sklepu', related_name='shop', db_column='shopID'),
        ),
    ]
