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
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nazwa', max_length=50)),
                ('slug', models.SlugField(unique=True, verbose_name='Nazwa w URL', max_length=30)),
                ('content', models.TextField(null=True, verbose_name='Treść', blank=True)),
                ('datetime', models.DateTimeField(verbose_name='Data publikacji')),
                ('visible_only_for_staff', models.BooleanField(verbose_name='Widoczne tylko dla administracji', default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'artykuł',
                'verbose_name_plural': 'artykuły',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nazwa', max_length=30)),
                ('slug', models.SlugField(unique=True, verbose_name='Nazwa w URL', max_length=20)),
            ],
            options={
                'verbose_name': 'kategoria',
                'verbose_name_plural': 'kategorie',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='wiki.Category', verbose_name='Kategoria'),
        ),
    ]
