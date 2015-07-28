# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='dimension',
            field=models.PositiveIntegerField(verbose_name='Wymiar', default=0),
        ),
        migrations.AlterField(
            model_name='door',
            name='owner',
            field=models.PositiveIntegerField(verbose_name='ID właściciela', default=0),
        ),
        migrations.AlterField(
            model_name='door',
            name='ownertype',
            field=models.PositiveSmallIntegerField(verbose_name='Typ właściciela', default=0, db_column='ownerType', choices=[(0, 'Brak'), (1, 'Postać'), (2, 'Grupa')]),
        ),
    ]
