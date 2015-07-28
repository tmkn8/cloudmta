# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0003_auto_20150728_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('skinid', models.PositiveSmallIntegerField(default=0, verbose_name='ID skinu', db_column='skinID')),
                ('skinname', models.CharField(max_length=100, verbose_name='nazwa ubrania', db_column='skinName')),
                ('price', models.PositiveSmallIntegerField(default=0, verbose_name='cena')),
                ('shopid', models.ForeignKey(to='doors.Door', verbose_name='drzwi', db_column='shopID')),
            ],
            options={
                'verbose_name': 'skiny na /ubrania',
                'db_table': '_clothes',
            },
        ),
        migrations.CreateModel(
            name='InteriorDetail',
            fields=[
                ('uid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='nazwa')),
                ('x', models.FloatField(default=0, verbose_name='pozycja X')),
                ('y', models.FloatField(default=0, verbose_name='pozycja Y')),
                ('z', models.FloatField(default=0, verbose_name='pozycja Z')),
                ('a', models.FloatField(default=0, verbose_name='kąt')),
                ('int', models.PositiveIntegerField(default=0, verbose_name='wnętrze')),
            ],
            options={
                'verbose_name_plural': 'Dane interiorów GTA',
                'verbose_name': 'Dane interioru GTA',
                'db_table': '_intlist',
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('model', models.PositiveIntegerField(verbose_name='ID modelu')),
                ('x', models.FloatField(default=0, verbose_name='pozycja X')),
                ('y', models.FloatField(default=0, verbose_name='pozycja Y')),
                ('z', models.FloatField(default=0, verbose_name='pozycja Z')),
                ('rx', models.FloatField(default=0, verbose_name='rotacja X')),
                ('ry', models.FloatField(default=0, verbose_name='rotacja Y')),
                ('rz', models.FloatField(default=0, verbose_name='rotacja Z')),
                ('interior', models.PositiveIntegerField(default=0, verbose_name='wnętrze')),
                ('dimension', models.PositiveIntegerField(default=0, verbose_name='wymiar')),
            ],
            options={
                'verbose_name_plural': 'obiekty',
                'verbose_name': 'obiekt',
                'db_table': '_objects',
            },
        ),
    ]
