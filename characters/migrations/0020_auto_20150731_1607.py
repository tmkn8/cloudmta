# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import characters.models
from django.conf import settings
import django_unixdatetimefield.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0019_auto_20150730_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='activated',
            field=models.BooleanField(verbose_name='aktywowana', help_text='stare, nie tykać', default=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='afktime',
            field=models.PositiveIntegerField(verbose_name='czas AFK', db_column='afkTime', help_text='w sekundach', default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='ajtime',
            field=models.PositiveIntegerField(verbose_name='czas AJ', db_column='ajTime', help_text='w sekundach', default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='angle',
            field=models.FloatField(null=True, verbose_name='kąt', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='blocked',
            field=models.BooleanField(verbose_name='zablokowana', default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='bwtime',
            field=models.PositiveIntegerField(verbose_name='czas BW', db_column='bwTime', help_text='w sekundach', default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='dimension',
            field=models.PositiveIntegerField(verbose_name='wymiar', default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='dob',
            field=models.DateField(verbose_name='data urodzenia'),
        ),
        migrations.AlterField(
            model_name='character',
            name='facecode',
            field=models.CharField(verbose_name='kod twarzy', db_column='faceCode', default=characters.models.Character.generate_facecode, unique=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='character',
            name='hide',
            field=models.BooleanField(verbose_name='ukryta', default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='hp',
            field=models.FloatField(verbose_name='punkty życia', default=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='ingame',
            field=models.BooleanField(verbose_name='postać w grze', default=False, db_column='inGame'),
        ),
        migrations.AlterField(
            model_name='character',
            name='interior',
            field=models.PositiveIntegerField(verbose_name='wnętrze', default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='lastvisit',
            field=django_unixdatetimefield.fields.UnixDateTimeField(null=True, db_column='lastVisit', verbose_name='ostatnia wizyta', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='memberid',
            field=models.ForeignKey(related_name='characters', related_query_name='character', verbose_name='konto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='character',
            name='money',
            field=models.PositiveIntegerField(verbose_name='gotówka', default=350),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(verbose_name='imię i nazwisko', help_text='drugie imię opcjonalne, odstępy rozdzielać spacją.', max_length=22, unique=True, validators=[django.core.validators.RegexValidator('^([A-Za-z]{2,})([\\s][A-Za-z]{2,})?([\\s][A-Za-z]{2,})$')]),
        ),
        migrations.AlterField(
            model_name='character',
            name='onlinetime',
            field=models.PositiveIntegerField(verbose_name='czas w grze', db_column='onlineTime', help_text='w sekundach', default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='sex',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Mężczyzna'), (2, 'Kobieta')], verbose_name='płeć'),
        ),
        migrations.AlterField(
            model_name='character',
            name='shortdna',
            field=models.CharField(db_column='shortDNA', unique=True, max_length=4, verbose_name='krótki kod DNA', default=characters.models.Character.generate_shortdna_code, help_text='używany m.in. do kominiarek'),
        ),
        migrations.AlterField(
            model_name='character',
            name='x',
            field=models.FloatField(null=True, verbose_name='pozycja X', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='y',
            field=models.FloatField(null=True, verbose_name='pozycja Y', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='z',
            field=models.FloatField(null=True, verbose_name='pozycja Z', blank=True),
        ),
        migrations.AlterField(
            model_name='startskin',
            name='sex',
            field=models.PositiveSmallIntegerField(choices=[(1, 'mężczyzna'), (2, 'kobieta')], verbose_name='płeć'),
        ),
    ]
