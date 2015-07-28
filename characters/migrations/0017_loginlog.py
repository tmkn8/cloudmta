# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0016_auto_20150718_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='ID')),
                ('ip', models.GenericIPAddressField(default='127.0.0.1', verbose_name='adres IP')),
                ('serial', models.CharField(null=True, verbose_name='serial', max_length=32, blank=True)),
                ('time', django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='data logowania')),
                ('charid', models.ForeignKey(to='characters.Character', db_column='charID', verbose_name='postać')),
            ],
            options={
                'verbose_name_plural': 'logi logowania',
                'verbose_name': 'log logowania',
                'db_table': '_login_logs',
            },
        ),
    ]
