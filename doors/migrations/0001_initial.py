# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='ID')),
                ('name', models.CharField(verbose_name='Nazwa', max_length=60)),
                ('ownertype', models.PositiveSmallIntegerField(choices=[(0, 'Brak'), (1, 'Postać'), (2, 'Grupa')], verbose_name='Typ właściciela', db_column='ownerType')),
                ('owner', models.PositiveIntegerField(verbose_name='ID właściciela')),
                ('dimension', models.PositiveIntegerField(verbose_name='Wymiar')),
            ],
            options={
                'verbose_name': 'drzwi',
                'verbose_name_plural': 'drzwi',
                'db_table': '_doors',
            },
        ),
        migrations.CreateModel(
            name='DoorPickup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='ID')),
                ('name', models.CharField(verbose_name='nazwa', max_length=255)),
                ('inx', models.FloatField(verbose_name='pozycja wejścia X', default=0, db_column='inX')),
                ('iny', models.FloatField(verbose_name='pozycja wejścia Y', default=0, db_column='inY')),
                ('inz', models.FloatField(verbose_name='pozycja wejścia Z', default=0, db_column='inZ')),
                ('outx', models.FloatField(verbose_name='pozycja wyjścia X', default=0, db_column='outX')),
                ('outy', models.FloatField(verbose_name='pozycja wyjścia Y', default=0, db_column='outY')),
                ('outz', models.FloatField(verbose_name='pozycja wyjścia Z', default=0, db_column='outZ')),
                ('indim', models.PositiveIntegerField(verbose_name='wymiar wejścia', default=0, db_column='inDim')),
                ('outdim', models.PositiveIntegerField(verbose_name='wymiar wyjścia', default=0, db_column='outDim')),
                ('inint', models.PositiveIntegerField(verbose_name='wnętrze wejścia', default=0, db_column='inInt')),
                ('outint', models.PositiveIntegerField(verbose_name='wnętrze wyjścia', default=0, db_column='outInt')),
                ('outmodel', models.PositiveIntegerField(verbose_name='model wyjścia', default=0, db_column='outModel')),
                ('inmodel', models.PositiveIntegerField(verbose_name='model wejścia', default=0, db_column='inModel')),
                ('inangle', models.FloatField(verbose_name='kąt wejścia', default=0, db_column='inAngle')),
                ('outangle', models.FloatField(verbose_name='kąt wyjścia', default=0, db_column='outAngle')),
                ('locked', models.BooleanField(verbose_name='Zamknięty', default=True, help_text='Czy pickup jest zamknięty?')),
                ('parentid', models.ForeignKey(db_column='parentID', to='doors.Door', verbose_name='drzwi')),
            ],
            options={
                'verbose_name': 'pickup drzwi',
                'verbose_name_plural': 'pickupy drzwi',
                'db_table': '_doorsPickup',
            },
        ),
    ]
