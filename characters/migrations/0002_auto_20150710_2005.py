# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='id',
            field=models.BigIntegerField(primary_key=True, db_column='ID', serialize=False, editable=False),
        ),
    ]
