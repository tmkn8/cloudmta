# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='flashtype',
            field=models.PositiveIntegerField(default=0, db_column='flashType'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='locked',
            field=models.BooleanField(default=True, verbose_name='Zamknięty'),
        ),
    ]
