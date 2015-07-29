# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Tytuł', max_length=50)),
                ('slug', models.SlugField(unique=True, max_length=30, verbose_name='nazwa w URL')),
                ('content', models.TextField(blank=True, help_text='Markdown', null=True, verbose_name='treść')),
                ('publish_date', models.DateTimeField(verbose_name='data opublikowania')),
                ('hidden', models.BooleanField(default=True, help_text='widoczny tylko dla członków ekipy z linkiem do postu', verbose_name='ukryty')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='autor')),
            ],
            options={
                'verbose_name': 'posty',
            },
        ),
    ]
