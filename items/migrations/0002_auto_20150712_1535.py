# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordertype',
            options={'verbose_name': 'Typ zamówień', 'verbose_name_plural': 'Typy zamówień'},
        ),
    ]
