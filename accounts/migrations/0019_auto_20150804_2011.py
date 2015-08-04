# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_user_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='strona internetowa'),
        ),
    ]
