# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_phonecontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposite',
            name='itemtype',
            field=models.IntegerField(choices=[(1, 'broń'), (2, 'amunicja'), (3, 'ubranie'), (4, 'megafon'), (5, 'kamizelka kuloodporna'), (6, 'jedzenie'), (7, 'ciało'), (8, 'telefon'), (9, 'rękawiczki'), (10, 'odznaka'), (11, 'identyfikator'), (12, 'płyta CD'), (13, 'narkotyki'), (14, 'paralizator'), (15, 'obiekt przyczepialny'), (16, 'maska'), (17, 'prawo jazdy'), (18, 'kajdanki'), (19, 'boombox'), (20, 'syrena policyjna'), (22, 'kostka do gry')], verbose_name='Typ produktu', db_column='itemType'),
        ),
    ]
