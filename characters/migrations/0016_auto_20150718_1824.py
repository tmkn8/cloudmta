# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0015_auto_20150713_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(help_text='Drugie imię opcjonalne, odstępy rozdzielać spacją.', max_length=22, validators=[django.core.validators.RegexValidator('^([A-Za-z]{2,})([\\s][A-Za-z]{2,})?([\\s][A-Za-z]{2,})$')], verbose_name='Imię i nazwisko', unique=True),
        ),
    ]
