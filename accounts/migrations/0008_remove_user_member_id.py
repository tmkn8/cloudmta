# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20150712_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='member_id',
        ),
    ]
