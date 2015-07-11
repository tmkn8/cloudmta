# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name_plural': 'Dostawy', 'verbose_name': 'Dostawa'},
        ),
        migrations.AlterModelOptions(
            name='deposite',
            options={'verbose_name_plural': 'Produkty w drzwiach', 'verbose_name': 'Produkt w drzwiach'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'Przedmioty', 'verbose_name': 'Przedmiot'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Produkty', 'verbose_name': 'Produkt'},
        ),
        migrations.AlterModelOptions(
            name='ordercategory',
            options={'verbose_name_plural': 'Kategorie produktów', 'verbose_name': 'Kategoria produktów'},
        ),
        migrations.AlterField(
            model_name='item',
            name='dimension',
            field=models.IntegerField(verbose_name='Wymiar', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, verbose_name='ID przedmiotu', serialize=False, db_column='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='interior',
            field=models.IntegerField(verbose_name='Interior', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='rx',
            field=models.FloatField(verbose_name='r X', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='ry',
            field=models.FloatField(verbose_name='r Y', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='rz',
            field=models.FloatField(verbose_name='r Z', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='slotid',
            field=models.IntegerField(verbose_name='Numer slotu w ekwipunku', default=0, db_column='slotID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='val1',
            field=models.IntegerField(verbose_name='Wartość 1', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='val2',
            field=models.IntegerField(verbose_name='Wartość 2', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='volume',
            field=models.IntegerField(verbose_name='Objętość', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='x',
            field=models.FloatField(verbose_name='Pozycja X', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='y',
            field=models.FloatField(verbose_name='Pozycja Y', default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='z',
            field=models.FloatField(verbose_name='Pozycja Z', default=0),
        ),
    ]
