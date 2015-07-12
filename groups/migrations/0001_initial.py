# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0014_auto_20150712_1650'),
        ('items', '0004_auto_20150712_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(db_column='ID', serialize=False, primary_key=True, verbose_name='ID grupy')),
                ('name', models.CharField(verbose_name='Nazwa', max_length=64)),
                ('tag', models.CharField(verbose_name='Tag', max_length=4)),
                ('r', models.PositiveSmallIntegerField(verbose_name='Kolor R', default=0)),
                ('g', models.PositiveSmallIntegerField(verbose_name='Kolor G', default=0)),
                ('b', models.PositiveSmallIntegerField(verbose_name='Kolor B', default=0)),
                ('perms', jsonfield.fields.JSONField(verbose_name='Uprawnienia grupy', blank=True, null=True)),
                ('cash', models.PositiveIntegerField(verbose_name='Pieniądze grupy', default=0)),
                ('ordertype', models.ForeignKey(db_column='orderType', to='items.OrderType', blank=True, verbose_name='Typ zamówienia', null=True)),
            ],
            options={
                'verbose_name': 'grupa',
                'verbose_name_plural': 'grupy',
                'db_table': '_groups',
            },
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(db_column='ID', serialize=False, primary_key=True)),
                ('groupid', models.ForeignKey(db_column='groupID', to='groups.Group', verbose_name='Grupa', related_name='groupmembers', related_query_name='groupmember')),
            ],
            options={
                'verbose_name': 'członek',
                'verbose_name_plural': 'członkowie',
                'db_table': '_groups_members',
            },
        ),
        migrations.CreateModel(
            name='GroupRank',
            fields=[
                ('id', models.AutoField(db_column='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Nazwa', default='Ranga', max_length=64)),
                ('cash', models.PositiveIntegerField(verbose_name='Wypłata', default=0)),
                ('defaultrank', models.BooleanField(db_column='defaultRank', help_text='Ranga, na którą trafiają nowi gracze. Musi być chociaż jedna w grupie.', verbose_name='Domyślna ranga', default=False)),
                ('perms', jsonfield.fields.JSONField(verbose_name='Uprawnienia', blank=True, null=True)),
                ('groupid', models.ForeignKey(db_column='groupID', to='groups.Group', verbose_name='Grupa', related_name='groupranks', related_query_name='grouprank')),
            ],
            options={
                'verbose_name': 'ranga',
                'verbose_name_plural': 'rangi',
                'db_table': '_groups_ranks',
            },
        ),
        migrations.AddField(
            model_name='groupmember',
            name='rankid',
            field=models.ForeignKey(db_column='rankID', to='groups.GroupRank', verbose_name='Ranga', related_name='groupsmembers', related_query_name='groupmembers'),
        ),
        migrations.AddField(
            model_name='groupmember',
            name='userid',
            field=models.ForeignKey(db_column='userID', to='characters.Character', verbose_name='Postać', related_name='characters', related_query_name='character'),
        ),
    ]
