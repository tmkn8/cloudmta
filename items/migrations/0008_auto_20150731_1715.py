# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20150730_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='cost',
            field=models.PositiveIntegerField(verbose_name='koszt', default=0, help_text='pieniądze'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='data',
            field=jsonfield.fields.JSONField(verbose_name='informacje o produkcie', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivergroup',
            field=models.ForeignKey(related_query_name='delivery', verbose_name='grupa kurierska', db_column='deliverGroup', related_name='deliveries', to='groups.Group'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='deliverid',
            field=models.ForeignKey(related_query_name='delivery', verbose_name='dostawca', related_name='deliveries', to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='intid',
            field=models.ForeignKey(help_text='do których dostaczany jest towar', verbose_name='drzwi', db_column='intID', to='doors.Door'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nazwa zamówienia'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='ordertype',
            field=models.ForeignKey(related_query_name='delivery', verbose_name='typ zamówienia', db_column='orderType', related_name='deliveries', to='items.OrderType'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='pieces',
            field=models.IntegerField(verbose_name='liczba sztuk', default=1),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='time',
            field=django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='czas', null=True, help_text='odebranie paczki przez kuriera', blank=True),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='intid',
            field=models.ForeignKey(related_query_name='deposite', verbose_name='drzwi', db_column='intID', related_name='deposites', to='doors.Door'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='itemval1',
            field=models.IntegerField(verbose_name='wartość produktu 1', default=0, db_column='itemVal1'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='itemval2',
            field=models.IntegerField(verbose_name='wartość produktu 2', default=0, db_column='itemVal2'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='itemval3',
            field=models.TextField(verbose_name='wartość produktu 3', db_column='itemVal3', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='itemvolume',
            field=models.IntegerField(verbose_name='objętość produktu', default=0, db_column='itemVolume'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nazwa produktu'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='stock',
            field=models.PositiveIntegerField(verbose_name='ilość', default=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='created',
            field=django_unixdatetimefield.fields.UnixDateTimeField(auto_now_add=True, verbose_name='data stworzenia przedmiotu'),
        ),
        migrations.AlterField(
            model_name='item',
            name='dimension',
            field=models.IntegerField(verbose_name='wymiar', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='interior',
            field=models.IntegerField(verbose_name='wnętrze', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='lastused',
            field=django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='ostatnio użyty', db_column='lastUsed', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='lastuseddata',
            field=jsonfield.fields.JSONField(verbose_name='odciski palców', db_column='lastUsedData', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=32, verbose_name='nazwa przedmiotu'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ownertype',
            field=models.PositiveSmallIntegerField(db_column='ownerType', choices=[(0, 'na ziemi'), (1, 'postać'), (3, 'pojazd'), (4, 'drzwi')], db_index=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='rx',
            field=models.FloatField(verbose_name='rotacja X', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='ry',
            field=models.FloatField(verbose_name='rotacja Y', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='rz',
            field=models.FloatField(verbose_name='rotacja Z', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='slotid',
            field=models.IntegerField(verbose_name='numer slotu w ekwipunku', default=0, db_column='slotID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.PositiveSmallIntegerField(verbose_name='typ przedmiotu', choices=[(1, 'broń'), (2, 'amunicja'), (3, 'ubranie'), (4, 'megafon'), (5, 'kamizelka kuloodporna'), (6, 'jedzenie'), (7, 'ciało'), (8, 'telefon'), (9, 'rękawiczki'), (10, 'odznaka'), (11, 'identyfikator'), (12, 'płyta CD'), (13, 'narkotyki'), (14, 'paralizator'), (15, 'obiekt przyczepialny'), (16, 'maska'), (17, 'prawo jazdy'), (18, 'kajdanki'), (19, 'boombox'), (20, 'syrena policyjna'), (22, 'kostka do gry')]),
        ),
        migrations.AlterField(
            model_name='item',
            name='used',
            field=models.BooleanField(verbose_name='w użytku', default=False, help_text='obecnie używany przez gracza'),
        ),
        migrations.AlterField(
            model_name='item',
            name='val1',
            field=models.IntegerField(verbose_name='wartość 1', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='val2',
            field=models.IntegerField(verbose_name='wartość 2', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='val3',
            field=models.TextField(verbose_name='wartość 3', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='volume',
            field=models.IntegerField(verbose_name='objętość', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='x',
            field=models.FloatField(verbose_name='pozycja X', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='y',
            field=models.FloatField(verbose_name='pozycja Y', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='z',
            field=models.FloatField(verbose_name='pozycja Z', default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nazwa produktu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordersize',
            field=models.IntegerField(verbose_name='rozmiar zamówienia', db_column='orderSize', help_text='w celu zapobiegania dostarczania dużych zamówień w małych pojazdach'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordertype',
            field=models.ForeignKey(related_query_name='order', verbose_name='typ zamówienia', db_column='orderType', related_name='orders', to='items.OrderType'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.PositiveIntegerField(verbose_name='cena produktu', default=0, help_text='pieniądze'),
        ),
        migrations.AlterField(
            model_name='ordercategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nazwa kategorii'),
        ),
        migrations.AlterField(
            model_name='ordercategory',
            name='orderowner',
            field=models.ForeignKey(related_query_name='ordercategory', verbose_name='grupa', db_column='orderOwner', related_name='ordercategories', to='groups.Group'),
        ),
        migrations.AlterField(
            model_name='ordercategory',
            name='ordertype',
            field=models.ForeignKey(related_query_name='ordercategory', verbose_name='typ zamówienia', db_column='orderType', related_name='ordercategories', to='items.OrderType'),
        ),
    ]
