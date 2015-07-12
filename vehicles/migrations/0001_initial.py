# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', verbose_name='ID pojazdu', primary_key=True)),
                ('name', models.CharField(verbose_name='Nazwa pojazdu', max_length=50)),
                ('ownertype', models.PositiveSmallIntegerField(db_column='ownerType', verbose_name='Typ właściciela', choices=[(0, 'Brak'), (1, 'Postać'), (2, 'Grupa')])),
                ('ownerid', models.IntegerField(help_text='ID właściciela', db_column='ownerID', verbose_name='Właściciel', default=0)),
                ('c1r', models.PositiveSmallIntegerField(help_text='Wprowadź kolor w formacie RGB', verbose_name='Kolor 1 R', default=0)),
                ('c1g', models.PositiveSmallIntegerField(help_text='Wprowadź kolor w formacie RGB', verbose_name='Kolor 1 G', default=0)),
                ('c1b', models.PositiveSmallIntegerField(help_text='Wprowadź kolor w formacie RGB', verbose_name='Kolor 1 B', default=0)),
                ('c2r', models.PositiveSmallIntegerField(help_text='Wprowadź kolor w formacie RGB', verbose_name='Kolor 2 R', default=0)),
                ('c2g', models.PositiveSmallIntegerField(help_text='Wprowadź kolor w formacie RGB', verbose_name='Kolor 2 G', default=0)),
                ('c2b', models.PositiveSmallIntegerField(help_text='Wprowadź kolor w formacie RGB', verbose_name='Kolor 2 B', default=0)),
                ('model', models.PositiveSmallIntegerField(help_text='ID modelu pojazud w MTA', verbose_name='Model')),
                ('hp', models.FloatField(help_text='Punkty życia pojazdu 0-1000', verbose_name='Stan pojazdu', default=0)),
                ('spawned', models.BooleanField(verbose_name='Zespawnowany', default=False)),
                ('locked', models.IntegerField(verbose_name='Zamknięty', default=True)),
                ('x', models.FloatField(verbose_name='Pozycja X', default=0)),
                ('y', models.FloatField(verbose_name='Pozycja Y', default=0)),
                ('z', models.FloatField(verbose_name='Pozycja Z', default=0)),
                ('rx', models.FloatField(verbose_name='Rotacja X', default=0)),
                ('ry', models.FloatField(verbose_name='Rotacja Y', default=0)),
                ('rz', models.FloatField(verbose_name='Rotacja Z', default=0)),
                ('v1', models.IntegerField(default=0)),
                ('v2', models.IntegerField(default=0)),
                ('fuel', models.FloatField(help_text='Ilość paliwa w baku', verbose_name='Paliwo', default=20)),
                ('maxfuel', models.PositiveSmallIntegerField(verbose_name='Pojemność baku', default=50)),
                ('damage', jsonfield.fields.JSONField(help_text='Szczegółowe zniszczenie poszczególnych części pojazdu', null=True, verbose_name='Zniszczenie pojazdu', blank=True)),
                ('interior', models.PositiveIntegerField(verbose_name='Wnętrze', default=0)),
                ('dimension', models.PositiveIntegerField(verbose_name='Wymiar', default=0)),
                ('flashtype', models.PositiveIntegerField(db_column='flashType')),
                ('distance', models.FloatField(verbose_name='Przebieg', default=0)),
                ('hasalarm', models.BooleanField(db_column='hasAlarm', verbose_name='Alarm', default=False)),
                ('handbrake', models.BooleanField(help_text='Hamulec ręczny zaciągnięty', verbose_name='Hamulec', default=True)),
                ('tireblock', models.BooleanField(db_column='tireBlock', verbose_name='Blokada na koło', default=False)),
            ],
            options={
                'db_table': '_vehicles',
            },
        ),
    ]
