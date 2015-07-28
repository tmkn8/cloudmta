# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20150728_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneContact',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='ID', serialize=False)),
                ('phoneid', models.PositiveIntegerField(verbose_name='ID telefonu', db_column='phoneID')),
                ('number', models.PositiveIntegerField(verbose_name='numer kontaktu')),
                ('name', models.CharField(verbose_name='nazwa kontaktu', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'kontakty telefoniczne',
                'verbose_name': 'kontakt telefoniczny',
                'db_table': '_phone_contacts',
            },
        ),
    ]
