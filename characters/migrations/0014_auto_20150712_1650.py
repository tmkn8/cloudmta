# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0013_auto_20150711_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'verbose_name': 'postać', 'verbose_name_plural': 'postacie'},
        ),
        migrations.AlterModelOptions(
            name='facecode',
            options={'verbose_name': 'kod twarzy', 'verbose_name_plural': 'kody twarzy'},
        ),
        migrations.AlterModelOptions(
            name='startskin',
            options={'verbose_name': 'skin startowy', 'verbose_name_plural': 'skiny startowe'},
        ),
    ]
