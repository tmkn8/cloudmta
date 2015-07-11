# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_auto_20150711_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='lastvisit',
            field=django_unixdatetimefield.fields.UnixDateTimeField(null=True, blank=True, verbose_name='Ostatnia wizyta', db_column='lastVisit'),
        ),
    ]
