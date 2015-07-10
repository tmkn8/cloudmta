# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_auto_20150710_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facecode',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('facecode', models.CharField(max_length=10, db_column='faceCode', help_text='Kod twarzy postaci, do której przypisany jest alias.', verbose_name='Kod twarzy')),
                ('name', models.CharField(max_length=100, verbose_name='Alias postaci')),
                ('charid', models.ForeignKey(db_column='charID', related_name='facecodes', verbose_name='Postać', to='characters.Character')),
            ],
            options={
                'db_table': '_faceCodes',
            },
        ),
    ]
