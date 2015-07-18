# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0015_auto_20150713_2341'),
        ('groups', '0006_auto_20150718_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupInvite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date', django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='Data zaproszenia')),
                ('character', models.ForeignKey(verbose_name='Postać', to='characters.Character')),
                ('group', models.ForeignKey(verbose_name='Grupa', to='groups.Group')),
                ('invited_by', models.ForeignKey(verbose_name='Zaproszony przez', to=settings.AUTH_USER_MODEL, help_text='Konto globalne, nie postać')),
            ],
            options={
                'verbose_name': 'zaproszenie do grupy',
                'verbose_name_plural': 'zaproszenia do grupy',
            },
        ),
    ]
