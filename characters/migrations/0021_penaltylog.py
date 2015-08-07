# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0020_auto_20150731_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenaltyLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='ID')),
                ('serial', models.CharField(max_length=32, verbose_name='serial')),
                ('ip', models.IPAddressField(verbose_name='adres IP')),
                ('reason', models.TextField(blank=True, verbose_name='powód', null=True)),
                ('time', django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='data nadania')),
                ('expire', django_unixdatetimefield.fields.UnixDateTimeField(blank=True, verbose_name='data wygaśnięcia', null=True)),
                ('type', models.CharField(max_length=1, choices=[(1, 'kick'), (2, 'admin jail'), (3, 'warn'), (4, 'ban'), (5, 'blokada postaci')], verbose_name='typ kary')),
                ('admin', models.ForeignKey(related_name='admins', to=settings.AUTH_USER_MODEL, related_query_name='admin', verbose_name='administrator', db_column='adminID')),
                ('character', models.ForeignKey(related_name='characters', to='characters.Character', related_query_name='character', verbose_name='administrator', db_column='userID')),
            ],
            options={
                'db_table': '_penalty_logs',
                'verbose_name': 'informacje o karze',
                'verbose_name_plural': 'logi kar',
            },
        ),
    ]
