# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_auto_20150710_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='lastvisit',
            field=django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='Ostatnia wizyta', blank=True, db_column='lastVisit', null=True),
        ),
    ]
