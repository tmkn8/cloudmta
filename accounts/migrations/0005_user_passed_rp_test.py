# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_quizquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passed_rp_test',
            field=models.BooleanField(default=False),
        ),
    ]
