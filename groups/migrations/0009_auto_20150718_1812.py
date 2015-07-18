# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_unixdatetimefield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0015_auto_20150713_2341'),
        ('groups', '0008_auto_20150718_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupInvitation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', django_unixdatetimefield.fields.UnixDateTimeField(verbose_name='Data zaproszenia', auto_now_add=True)),
                ('character', models.ForeignKey(related_query_name='groupinvitation', to='characters.Character', related_name='groupinvitations', verbose_name='Postać')),
                ('group', models.ForeignKey(related_query_name='groupinvitation', to='groups.Group', related_name='groupinvitations', verbose_name='Grupa')),
                ('invited_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, help_text='Konto globalne, nie postać', verbose_name='Zaproszony przez')),
            ],
            options={
                'verbose_name': 'zaproszenie do grupy',
                'verbose_name_plural': 'zaproszenia do grupy',
            },
        ),
        migrations.RemoveField(
            model_name='groupinvite',
            name='character',
        ),
        migrations.RemoveField(
            model_name='groupinvite',
            name='group',
        ),
        migrations.RemoveField(
            model_name='groupinvite',
            name='invited_by',
        ),
        migrations.DeleteModel(
            name='GroupInvite',
        ),
    ]
