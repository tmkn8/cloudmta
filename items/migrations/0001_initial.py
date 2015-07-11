# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0013_auto_20150711_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(verbose_name='ID dostarczenia', primary_key=True, db_column='ID', serialize=False)),
                ('intid', models.IntegerField(help_text='Do których dostaczany jest towar', db_column='intID', verbose_name='Drzwi')),
                ('pieces', models.IntegerField(default=1, verbose_name='Liczba sztuk')),
                ('data', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Informacje o produkcie')),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa zamówienia')),
                ('delivergroup', models.IntegerField(default=0, db_column='deliverGroup')),
                ('time', django_unixdatetimefield.fields.UnixDateTimeField(blank=True, help_text='Odebranie paczki przez kuriera', null=True, verbose_name='Czas')),
                ('cost', models.PositiveIntegerField(help_text='Pieniądze', default=0, verbose_name='Koszt')),
                ('deliverid', models.ForeignKey(related_query_name='delivery', related_name='deliveries', verbose_name='Dostawca', to='characters.Character')),
            ],
            options={
                'verbose_name_plural': 'Dostawy',
                'verbose_name': 'Dostawa',
                'db_table': '_delivers',
            },
        ),
        migrations.CreateModel(
            name='Deposite',
            fields=[
                ('id', models.AutoField(verbose_name='ID depozytu', primary_key=True, db_column='ID', serialize=False)),
                ('intid', models.IntegerField(db_column='intID', verbose_name='Drzwi')),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa produktu')),
                ('stock', models.PositiveIntegerField(default=1, verbose_name='Ilość')),
                ('itemtype', models.IntegerField(choices=[(1, 'Jakiś typ')], db_column='itemType', verbose_name='Typ produktu')),
                ('itemval1', models.IntegerField(default=0, db_column='itemVal1', verbose_name='Wartość produktu 1')),
                ('itemval2', models.IntegerField(default=0, db_column='itemVal2', verbose_name='Wartość produktu 2')),
                ('itemval3', models.TextField(verbose_name='Wartość produktu 3', blank=True, null=True, db_column='itemVal3')),
                ('itemvolume', models.IntegerField(default=0, db_column='itemVolume', verbose_name='Objętość produktu')),
            ],
            options={
                'verbose_name_plural': 'Produkty w drzwiach',
                'verbose_name': 'Produkt w drzwiach',
                'db_table': '_deposite',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID przedmiotu', primary_key=True, db_column='ID', serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='Nazwa przedmiotu')),
                ('ownertype', models.PositiveSmallIntegerField(choices=[(0, 'Na ziemi'), (1, 'Postać'), (3, 'Pojazd'), (4, 'Drzwi')], db_index=True, db_column='ownerType')),
                ('owner', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='ID właściciela')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Jakiś typ')], verbose_name='Typ przedmiotu')),
                ('slotid', models.IntegerField(default=0, db_column='slotID', verbose_name='Numer slotu w ekwipunku')),
                ('val1', models.IntegerField(default=0, verbose_name='Wartość 1')),
                ('val2', models.IntegerField(default=0, verbose_name='Wartość 2')),
                ('val3', models.TextField(blank=True, null=True, verbose_name='Wartość 3')),
                ('volume', models.IntegerField(default=0, verbose_name='Objętość')),
                ('created', django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='Data stworzenia przedmiotu', auto_now_add=True)),
                ('lastused', django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='Ostatnio użyty', blank=True, null=True, db_column='lastUsed')),
                ('lastuseddata', jsonfield.fields.JSONField(verbose_name='Odciski palców', blank=True, null=True, db_column='lastUsedData')),
                ('used', models.BooleanField(help_text='Obecnie używany przez gracza', default=False, verbose_name='W użytku')),
                ('x', models.FloatField(default=0, verbose_name='Pozycja X')),
                ('y', models.FloatField(default=0, verbose_name='Pozycja Y')),
                ('z', models.FloatField(default=0, verbose_name='Pozycja Z')),
                ('rx', models.FloatField(default=0, verbose_name='r X')),
                ('ry', models.FloatField(default=0, verbose_name='r Y')),
                ('rz', models.FloatField(default=0, verbose_name='r Z')),
                ('interior', models.IntegerField(default=0, verbose_name='Interior')),
                ('dimension', models.IntegerField(default=0, verbose_name='Wymiar')),
            ],
            options={
                'verbose_name_plural': 'Przedmioty',
                'verbose_name': 'Przedmiot',
                'db_table': '_items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID produktu', primary_key=True, db_column='ID', serialize=False)),
                ('ordersize', models.IntegerField(help_text='W celu zapobiegania dostarczania dużych zamówień w małych pojazdach', db_column='orderSize', verbose_name='Rozmiar zamówienia')),
                ('data', jsonfield.fields.JSONField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(help_text='Pieniądze', default=0, verbose_name='Cena produktu')),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa produktu')),
            ],
            options={
                'verbose_name_plural': 'Produkty',
                'verbose_name': 'Produkt',
                'db_table': '_orders',
            },
        ),
        migrations.CreateModel(
            name='OrderCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID kategorii', primary_key=True, db_column='ID', serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa kategorii')),
                ('orderowner', models.IntegerField(default=0, db_column='orderOwner', verbose_name='Grupa')),
            ],
            options={
                'verbose_name_plural': 'Kategorie produktów',
                'verbose_name': 'Kategoria produktów',
                'db_table': '_ordersCat',
            },
        ),
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='ordercategory',
            name='ordertype',
            field=models.ForeignKey(related_query_name='ordercategory', to='items.OrderType', related_name='ordercategories', db_column='orderType', verbose_name='Typ zamówienia'),
        ),
        migrations.AddField(
            model_name='order',
            name='catid',
            field=models.ForeignKey(related_name='category', db_column='catID', to='items.OrderCategory'),
        ),
        migrations.AddField(
            model_name='order',
            name='ordertype',
            field=models.ForeignKey(related_query_name='order', to='items.OrderType', related_name='orders', db_column='orderType', verbose_name='Typ zamówienia'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='ordertype',
            field=models.ForeignKey(related_query_name='delivery', to='items.OrderType', related_name='deliveries', db_column='orderType', verbose_name='Typ zamówienia'),
        ),
    ]
