# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0005_auto_20150728_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreeDText',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('x', models.FloatField(default=0, verbose_name='pozycja X')),
                ('y', models.FloatField(default=0, verbose_name='pozycja Y')),
                ('z', models.FloatField(default=0, verbose_name='pozycja Z')),
                ('vw', models.PositiveIntegerField(default=0, verbose_name='wymiar')),
                ('int', models.PositiveIntegerField(default=0, verbose_name='wnętrze')),
                ('text', models.TextField(blank=True, verbose_name='treść', null=True)),
                ('r', models.PositiveSmallIntegerField(default=0, verbose_name='kolor R')),
                ('g', models.PositiveSmallIntegerField(default=0, verbose_name='kolor G')),
                ('b', models.PositiveSmallIntegerField(default=0, verbose_name='kolor B')),
            ],
            options={
                'verbose_name': 'etykieta 3W',
                'verbose_name_plural': 'etykiety 3W',
                'db_table': '_3Dtexts',
            },
        ),
    ]
