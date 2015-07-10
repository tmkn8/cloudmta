# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20150710_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='id',
            field=models.AutoField(primary_key=True, db_column='ID', serialize=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='memberid',
            field=models.BigIntegerField(help_text='Konto globalne', verbose_name='ID użytkownika', db_index=True, db_column='memberID'),
        ),
    ]
