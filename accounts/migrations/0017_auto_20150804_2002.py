# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20150804_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.CharField(null=True, verbose_name='Facebook', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('F', 'kobieta'), ('M', 'mężczyzna'), ('N', 'żadna z powyższych')], null=True, blank=True, max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.CharField(null=True, verbose_name='Instagram', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(null=True, verbose_name='miejscowość', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='rgsc',
            field=models.CharField(null=True, verbose_name='Rockstar Games Social Club', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='steam',
            field=models.CharField(null=True, verbose_name='Steam', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='tumblr',
            field=models.CharField(null=True, verbose_name='Twitter', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(null=True, verbose_name='Twitter', blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.BooleanField(default=False, verbose_name='adres e-mail widoczny publicznie'),
        ),
    ]
