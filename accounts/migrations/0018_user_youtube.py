# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20150804_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='youtube',
            field=models.CharField(blank=True, null=True, verbose_name='YouTube', max_length=100),
        ),
    ]
