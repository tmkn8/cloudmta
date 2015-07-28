# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0002_auto_20150728_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='ID', serialize=False)),
                ('price', models.PositiveIntegerField(verbose_name='Cena')),
                ('itemname', models.CharField(max_length=255, db_column='itemName', verbose_name='nazwa przedmiotu')),
                ('itemtype', models.PositiveSmallIntegerField(choices=[(1, 'broń'), (2, 'amunicja'), (3, 'ubranie'), (4, 'megafon'), (5, 'kamizelka kuloodporna'), (6, 'jedzenie'), (7, 'ciało'), (8, 'telefon'), (9, 'rękawiczki'), (10, 'odznaka'), (11, 'identyfikator'), (12, 'płyta CD'), (13, 'narkotyki'), (14, 'paralizator'), (15, 'obiekt przyczepialny'), (16, 'maska'), (17, 'prawo jazdy'), (18, 'kajdanki'), (19, 'boombox'), (20, 'syrena policyjna'), (22, 'kostka do gry')], db_column='itemType', verbose_name='typ przedmiotu')),
                ('itemval1', models.IntegerField(default=0, db_column='itemVal1', verbose_name='Wartość przedmiotu 1')),
                ('itemval2', models.IntegerField(default=0, db_column='itemVal2', verbose_name='Wartość przedmiotu 2')),
                ('itemval3', models.TextField(db_column='itemVal3', blank=True, null=True, verbose_name='Wartość przedmiotu 3')),
                ('itemvolume', models.IntegerField(default=0, db_column='itemVolume', verbose_name='Objętość przedmiotu')),
            ],
            options={
                'db_table': '_shops',
                'verbose_name_plural': 'produkty na /kup',
                'verbose_name': 'produkt na /kup',
            },
        ),
        migrations.AlterField(
            model_name='door',
            name='dimension',
            field=models.PositiveIntegerField(default=0, verbose_name='wymiar'),
        ),
        migrations.AlterField(
            model_name='door',
            name='name',
            field=models.CharField(max_length=60, verbose_name='nazwa'),
        ),
        migrations.AlterField(
            model_name='door',
            name='ownertype',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, 'Brak'), (1, 'Postać'), (2, 'Grupa')], db_column='ownerType', verbose_name='typ właściciela'),
        ),
        migrations.AlterField(
            model_name='doorpickup',
            name='locked',
            field=models.BooleanField(help_text='czy pickup (drzwi) jest zamknięty', default=True, verbose_name='zamknięty'),
        ),
        migrations.AddField(
            model_name='shop',
            name='shopid',
            field=models.ForeignKey(to='doors.Door', verbose_name='drzwi sklepu', db_column='shopID'),
        ),
    ]
