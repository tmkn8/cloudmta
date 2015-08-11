# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20150810_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', blank=True, to=settings.AUTH_USER_MODEL, verbose_name='znajomi'),
        ),
    ]
