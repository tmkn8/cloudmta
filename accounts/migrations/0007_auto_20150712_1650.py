# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20150711_0022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'managed': False, 'verbose_name': 'użytkownik forum', 'verbose_name_plural': 'użytkownicy forum'},
        ),
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'verbose_name': 'pytanie z testu wiedzy RP', 'verbose_name_plural': 'pytania z testu wiedzy RP'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'użytkownik Django', 'verbose_name_plural': 'użytkownicy Django'},
        ),
    ]
