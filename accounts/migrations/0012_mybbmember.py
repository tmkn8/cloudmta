# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20150731_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBBMember',
            fields=[
                ('uid', models.AutoField(verbose_name='UID', primary_key=True, serialize=False)),
                ('username', models.CharField(verbose_name='Nazwa użytkownika', max_length=120)),
                ('email', models.EmailField(verbose_name='Adres e-mail', max_length=220)),
                ('password', models.CharField(verbose_name='Hasło', editable=False, max_length=120)),
                ('salt', models.CharField(verbose_name='Sól', editable=False, max_length=10)),
            ],
            options={
                'verbose_name': 'użytkownik forum',
                'verbose_name_plural': 'użytkownicy forum',
                'db_table': 'mybb_users',
                'managed': False,
            },
        ),
    ]
