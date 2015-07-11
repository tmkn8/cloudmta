# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20150711_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='cost',
            field=models.PositiveIntegerField(verbose_name='Koszt', default=0, help_text='Pieniądze'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='data',
            field=jsonfield.fields.JSONField(verbose_name='Informacje o produkcie', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivergroup',
            field=models.IntegerField(db_column='deliverGroup', default=0),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='deliverid',
            field=models.ForeignKey(to='characters.Character', related_query_name='delivery', related_name='deliveries', verbose_name='Dostawca'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='id',
            field=models.AutoField(serialize=False, db_column='ID', primary_key=True, verbose_name='ID dostarczenia'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='intid',
            field=models.IntegerField(db_column='intID', help_text='Do których dostaczany jest towar', verbose_name='Drzwi'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(verbose_name='Nazwa zamówienia', max_length=255),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='ordertype',
            field=models.ForeignKey(to='items.OrderType', related_query_name='delivery', related_name='deliveries', db_column='orderType', verbose_name='Typ zamówienia'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='pieces',
            field=models.IntegerField(default=1, verbose_name='Liczba sztuk'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='time',
            field=django_unixdatetimefield.fields.UnixDateTimeField(null=True, verbose_name='Czas', help_text='Odebranie paczki przez kuriera', blank=True),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='id',
            field=models.AutoField(serialize=False, db_column='ID', primary_key=True, verbose_name='ID depozytu'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='intid',
            field=models.IntegerField(db_column='intID', verbose_name='Drzwi'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='itemtype',
            field=models.IntegerField(choices=[(1, 'Jakiś typ')], db_column='itemType', verbose_name='Typ produktu'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='itemval1',
            field=models.IntegerField(db_column='itemVal1', default=0, verbose_name='Wartość produktu 1'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='itemval2',
            field=models.IntegerField(db_column='itemVal2', default=0, verbose_name='Wartość produktu 2'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='itemval3',
            field=models.TextField(verbose_name='Wartość produktu 3', db_column='itemVal3', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='itemvolume',
            field=models.IntegerField(db_column='itemVolume', default=0, verbose_name='Objętość produktu'),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='name',
            field=models.CharField(verbose_name='Nazwa produktu', max_length=255),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='stock',
            field=models.PositiveIntegerField(default=1, verbose_name='Ilość'),
        ),
        migrations.AlterField(
            model_name='order',
            name='catid',
            field=models.ForeignKey(to='items.OrderCategory', related_name='category', db_column='catID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='data',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(serialize=False, db_column='ID', primary_key=True, verbose_name='ID produktu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(verbose_name='Nazwa produktu', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordersize',
            field=models.IntegerField(verbose_name='Rozmiar zamówienia', db_column='orderSize', default=0, help_text='W celu zapobiegania dostarczania dużych zamówień w małych pojazdach'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='ordertype',
            field=models.ForeignKey(to='items.OrderType', related_query_name='order', related_name='orders', db_column='orderType', verbose_name='Typ zamówienia'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Cena produktu', default=0, help_text='Pieniądze'),
        ),
        migrations.AlterField(
            model_name='ordercategory',
            name='id',
            field=models.AutoField(serialize=False, db_column='ID', primary_key=True, verbose_name='ID kategorii'),
        ),
        migrations.AlterField(
            model_name='ordercategory',
            name='name',
            field=models.CharField(verbose_name='Nazwa kategorii', max_length=255),
        ),
        migrations.AlterField(
            model_name='ordercategory',
            name='orderowner',
            field=models.IntegerField(db_column='orderOwner', default=0, verbose_name='Grupa'),
        ),
        migrations.AlterField(
            model_name='ordercategory',
            name='ordertype',
            field=models.ForeignKey(to='items.OrderType', related_query_name='ordercategory', related_name='ordercategories', db_column='orderType', verbose_name='Typ zamówienia'),
        ),
    ]
