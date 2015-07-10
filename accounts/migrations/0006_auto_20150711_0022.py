# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_passed_rp_test'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'verbose_name_plural': 'Pytania z testu wiedzy RP', 'verbose_name': 'Pytanie z testu wiedzy RP'},
        ),
    ]
