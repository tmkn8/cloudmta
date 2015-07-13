# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0014_auto_20150712_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='memberid',
            field=models.ForeignKey(related_name='characters', verbose_name='Konto', related_query_name='character', to=settings.AUTH_USER_MODEL),
        ),
    ]
