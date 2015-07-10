# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import characters.models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0011_auto_20150711_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='dna',
            field=models.CharField(max_length=255, default=characters.models.Character.generate_dna_code, unique=True, verbose_name='DNA', db_column='DNA'),
        ),
        migrations.AlterField(
            model_name='character',
            name='facecode',
            field=models.CharField(max_length=6, default=characters.models.Character.generate_facecode, unique=True, verbose_name='Kod twarzy', db_column='faceCode'),
        ),
        migrations.AlterField(
            model_name='character',
            name='shortdna',
            field=models.CharField(help_text='Używany m.in. do kominiarek', default=characters.models.Character.generate_shortdna_code, db_column='shortDNA', max_length=4, unique=True, verbose_name='Krótki kod DNA'),
        ),
    ]
