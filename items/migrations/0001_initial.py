# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('intid', models.IntegerField(db_column='intID')),
                ('pieces', models.IntegerField()),
                ('data', jsonfield.fields.JSONField()),
                ('name', models.CharField(max_length=255)),
                ('ordertype', models.IntegerField(db_column='orderType')),
                ('delivergroup', models.IntegerField(db_column='deliverGroup')),
                ('deliverid', models.IntegerField(db_column='deliverID')),
                ('time', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': '_delivers',
            },
        ),
        migrations.CreateModel(
            name='Deposite',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('intid', models.IntegerField(db_column='intID')),
                ('name', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('itemtype', models.IntegerField(db_column='itemType')),
                ('itemval1', models.IntegerField(db_column='itemVal1')),
                ('itemval2', models.IntegerField(db_column='itemVal2')),
                ('itemval3', models.CharField(db_column='itemVal3', max_length=255)),
                ('itemvolume', models.IntegerField(db_column='itemVolume')),
            ],
            options={
                'managed': False,
                'db_table': '_deposite',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('ordersize', models.IntegerField(null=True, db_column='orderSize', blank=True)),
                ('catid', models.IntegerField(db_column='catID')),
                ('data', jsonfield.fields.JSONField()),
                ('price', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('ordertype', models.IntegerField(db_column='orderType')),
            ],
            options={
                'managed': False,
                'db_table': '_orders',
            },
        ),
        migrations.CreateModel(
            name='OrderCategory',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('ordertype', models.IntegerField(db_column='orderType')),
                ('orderowner', models.IntegerField(db_column='orderOwner')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': '_ordersCat',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, db_column='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Nazwa przedmiotu', max_length=32)),
                ('ownertype', models.PositiveSmallIntegerField(db_column='ownerType', choices=[(0, 'Na ziemi'), (1, 'Postać'), (3, 'Pojazd'), (4, 'Drzwi')], db_index=True)),
                ('owner', models.IntegerField(null=True, verbose_name='ID właściciela', blank=True, db_index=True)),
                ('type', models.PositiveSmallIntegerField(verbose_name='Typ przedmiotu', choices=[(1, 'Jakiś typ')])),
                ('slotid', models.IntegerField(verbose_name='Numer slotu w ekwipunku', null=True, db_column='slotID', blank=True)),
                ('val1', models.IntegerField(null=True, verbose_name='Wartość 1', blank=True)),
                ('val2', models.IntegerField(null=True, verbose_name='Wartość 2', blank=True)),
                ('val3', models.TextField(null=True, verbose_name='Wartość 3', blank=True)),
                ('volume', models.IntegerField(null=True, verbose_name='Objętość', blank=True)),
                ('created', django_unixdatetimefield.fields.UnixDateTimeField(auto_now_add=True, verbose_name='Data stworzenia przedmiotu')),
                ('lastused', django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='Ostatnio użyty', null=True, db_column='lastUsed', blank=True)),
                ('lastuseddata', jsonfield.fields.JSONField(verbose_name='Odciski palców', null=True, db_column='lastUsedData', blank=True)),
                ('used', models.BooleanField(default=False, help_text='Obecnie używany przez gracza', verbose_name='W użytku')),
                ('x', models.FloatField(null=True, blank=True)),
                ('y', models.FloatField(null=True, blank=True)),
                ('z', models.FloatField(null=True, blank=True)),
                ('rx', models.FloatField(null=True, blank=True)),
                ('ry', models.FloatField(null=True, blank=True)),
                ('rz', models.FloatField(null=True, blank=True)),
                ('interior', models.IntegerField(null=True, blank=True)),
                ('dimension', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': '_items',
            },
        ),
    ]
