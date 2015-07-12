# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_auto_20150712_1648'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name': 'pojazd', 'verbose_name_plural': 'pojazdy'},
        ),
    ]
