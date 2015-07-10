# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_startskin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startskin',
            name='skin_id',
            field=models.PositiveSmallIntegerField(unique=True, verbose_name='ID skina'),
        ),
    ]
