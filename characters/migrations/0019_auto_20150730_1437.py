# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0018_auto_20150728_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='activated',
            field=models.BooleanField(help_text='Stare, nie tykać', verbose_name='Aktywowana', default=True),
        ),
    ]
