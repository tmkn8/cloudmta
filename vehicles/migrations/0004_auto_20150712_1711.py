# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20150712_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='flashtype',
            field=models.PositiveIntegerField(verbose_name='Typ świateł emergency', default=0, db_column='flashType', choices=[(0, 'Brak'), (1, 'Światła PD'), (2, 'Światła FD')]),
        ),
    ]
