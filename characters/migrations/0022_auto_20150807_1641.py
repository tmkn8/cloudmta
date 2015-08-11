# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0021_penaltylog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penaltylog',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='adres IP'),
        ),
    ]
