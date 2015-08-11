# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_mybbmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(verbose_name='Znajomi', related_name='friends_rel_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
