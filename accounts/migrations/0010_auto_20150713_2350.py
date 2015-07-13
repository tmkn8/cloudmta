# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20150713_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(help_text='Ma dostęp do strony administracji.', default=False, verbose_name='Ekipa'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passed_rp_test',
            field=models.BooleanField(default=False, verbose_name='Zdał test RP'),
        ),
    ]
