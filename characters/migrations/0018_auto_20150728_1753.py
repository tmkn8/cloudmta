# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0017_loginlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginlog',
            name='time',
            field=django_unixdatetimefield.fields.UnixDateTimeField(null=True, verbose_name='data logowania', blank=True),
        ),
    ]
