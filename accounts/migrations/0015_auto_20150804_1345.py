# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20150803_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.TextField(help_text='markdown', blank=True, verbose_name='O mnie', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, blank=True, verbose_name='Awatar', upload_to='user-avatars'),
        ),
        migrations.AddField(
            model_name='user',
            name='public_email',
            field=models.BooleanField(verbose_name='adres e-mail widoczny publicznie', default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='skype_id',
            field=models.CharField(null=True, blank=True, verbose_name='identyfikator skype', max_length=40),
        ),
    ]
