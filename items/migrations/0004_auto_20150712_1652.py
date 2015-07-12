# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20150712_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'dostawa', 'verbose_name_plural': 'dostawy'},
        ),
        migrations.AlterModelOptions(
            name='deposite',
            options={'verbose_name': 'produkt w drzwiach', 'verbose_name_plural': 'produkty w drzwiach'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'przedmiot', 'verbose_name_plural': 'przedmioty'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'produkt', 'verbose_name_plural': 'produkty'},
        ),
        migrations.AlterModelOptions(
            name='ordercategory',
            options={'verbose_name': 'kategoria produktów', 'verbose_name_plural': 'kategorie produktów'},
        ),
        migrations.AlterModelOptions(
            name='ordertype',
            options={'verbose_name': 'typ zamówień', 'verbose_name_plural': 'typy zamówień'},
        ),
    ]
