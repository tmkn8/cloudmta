# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True, db_column='ID')),
                ('memberid', models.BigIntegerField(verbose_name='ID użytkownika', db_column='memberID', db_index=True)),
                ('name', models.CharField(verbose_name='Imię i nazwisko', max_length=22, help_text='Drugie imię opcjonalne, odstępy rozdzielać spacją.', validators=[django.core.validators.RegexValidator('^([A-Za-z]{2,})([\\s][A-Za-z]{2,})?([\\s][A-Za-z]{2,})$')])),
                ('facecode', models.CharField(verbose_name='Kod twarzy', unique=True, max_length=6, db_column='faceCode')),
                ('shortdna', models.CharField(verbose_name='Krótki kod DNA', unique=True, max_length=4, db_column='shortDNA', help_text='Używany m.in. do kominiarek')),
                ('dna', models.CharField(verbose_name='DNA', unique=True, max_length=255, db_column='DNA')),
                ('hp', models.FloatField(verbose_name='Punkty życia', default=100)),
                ('skin', models.PositiveSmallIntegerField(verbose_name='ID Skina', default=1)),
                ('x', models.FloatField(verbose_name='Pozycja X', blank=True, null=True)),
                ('y', models.FloatField(verbose_name='Pozycja Y', blank=True, null=True)),
                ('z', models.FloatField(verbose_name='Pozycja Z', blank=True, null=True)),
                ('angle', models.FloatField(verbose_name='Kąt', blank=True, null=True)),
                ('dimension', models.PositiveIntegerField(verbose_name='Wymiar', default=0)),
                ('interior', models.PositiveIntegerField(verbose_name='Wnętrze', default=0)),
                ('money', models.PositiveIntegerField(verbose_name='Gotówka', default=350)),
                ('bwtime', models.PositiveIntegerField(verbose_name='Czas BW', default=0, db_column='bwTime', help_text='W sekundach')),
                ('ajtime', models.PositiveIntegerField(verbose_name='Czas AJ', default=0, db_column='ajTime', help_text='W sekundach')),
                ('onlinetime', models.PositiveIntegerField(verbose_name='Czas w grze', default=0, db_column='onlineTime', help_text='W sekundach')),
                ('afktime', models.PositiveIntegerField(verbose_name='Czas AFK', default=0, db_column='afkTime', help_text='W sekundach')),
                ('sex', models.PositiveSmallIntegerField(verbose_name='Płeć', choices=[(1, 'Mężczyzna'), (2, 'Kobieta')])),
                ('ingame', models.BooleanField(verbose_name='Postać w grze', db_column='inGame')),
                ('lastvisit', django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='Ostatnia wizyta', db_column='lastVisit')),
                ('blocked', models.BooleanField(verbose_name='Zablokowana', default=False)),
                ('hide', models.BooleanField(verbose_name='Ukryta', default=False)),
                ('dob', models.DateField(verbose_name='Data urodzenia')),
                ('activated', models.BooleanField(verbose_name='Aktywowana', default=False)),
            ],
            options={
                'db_table': '_characters',
                'verbose_name_plural': 'Postacie',
                'verbose_name': 'Postać',
            },
        ),
    ]
