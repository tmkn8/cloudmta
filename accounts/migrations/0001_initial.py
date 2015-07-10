# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('uid', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=220)),
                ('password', models.CharField(max_length=120)),
                ('salt', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'mybb_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('username', models.CharField(verbose_name='Nazwa użytkownika', unique=True, editable=False, max_length=20, validators=[django.core.validators.RegexValidator('^([A-Za-z0-9]{3,})$')])),
                ('email', models.EmailField(verbose_name='Adres e-mail', unique=True, editable=False, max_length=254)),
                ('member_id', models.IntegerField(verbose_name='ID konta na forum', unique=True, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
