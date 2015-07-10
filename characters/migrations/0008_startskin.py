# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_auto_20150710_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartSkin',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('skin_id', models.PositiveSmallIntegerField(verbose_name='ID skina')),
                ('sex', models.PositiveSmallIntegerField(choices=[(1, 'Mężczyzna'), (2, 'Kobieta')], verbose_name='Płeć')),
            ],
            options={
                'verbose_name_plural': 'Skiny startowe',
                'verbose_name': 'Skin startowy',
            },
        ),
    ]
