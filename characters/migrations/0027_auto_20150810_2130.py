# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0026_auto_20150810_1851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='penaltylog',
            options={'verbose_name': 'informacje o karze', 'verbose_name_plural': 'logi kar', 'ordering': ['-time']},
        ),
    ]
