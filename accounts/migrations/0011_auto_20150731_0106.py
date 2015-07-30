# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20150713_2350'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(verbose_name='data dołączenia', default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(verbose_name='czy konto jest aktywne', default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='adres e-mail', unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(verbose_name='ekipa', default=False, help_text='ma dostęp do strony administracji.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passed_rp_test',
            field=models.BooleanField(verbose_name='zdał test RP', default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^([A-Za-z0-9]{3,})$')], verbose_name='nazwa użytkownika', unique=True, max_length=20),
        ),
    ]
