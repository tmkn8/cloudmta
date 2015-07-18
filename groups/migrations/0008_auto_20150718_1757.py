# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_groupinvite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupinvite',
            name='date',
            field=django_unixdatetimefield.fields.UnixDateTimeField(auto_now_add=True, verbose_name='Data zaproszenia'),
        ),
    ]
