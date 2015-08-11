# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20150804_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cover_photo',
            field=models.ImageField(null=True, upload_to='cover_photos', verbose_name='okładka profilu', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='about_me',
            field=models.TextField(help_text='markdown', null=True, verbose_name='o mnie', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='user-avatars', verbose_name='awatar', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to=settings.AUTH_USER_MODEL, verbose_name='znajomi'),
        ),
    ]
