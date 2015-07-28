# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0004_clothes_interiordetail_object'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interiordetail',
            options={'verbose_name': 'dane interioru GTA', 'verbose_name_plural': 'dane interiorów GTA'},
        ),
    ]
