# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_facecode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facecode',
            options={'verbose_name_plural': 'Kody twarzy', 'verbose_name': 'Kod twarzy'},
        ),
        migrations.AlterField(
            model_name='character',
            name='lastvisit',
            field=django_unixdatetimefield.fields.UnixDateTimeField(blank=True, null=True, editable=False, verbose_name='Ostatnia wizyta', db_column='lastVisit'),
        ),
    ]
