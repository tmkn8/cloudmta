# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20150804_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(verbose_name='znajomi', related_name='friends_rel_+', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
