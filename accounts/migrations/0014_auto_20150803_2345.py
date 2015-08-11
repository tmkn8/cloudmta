# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_user_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sent_time', models.DateTimeField(verbose_name='czas zaproszenia', auto_now_add=True)),
                ('invited', models.ForeignKey(verbose_name='zaproszony użytkownik', related_query_name='friend_invited', to=settings.AUTH_USER_MODEL, related_name='friends_invited')),
                ('invited_by', models.ForeignKey(verbose_name='zapraszający', related_query_name='friend_invited_by', to=settings.AUTH_USER_MODEL, related_name='friends_invited_by')),
            ],
            options={
                'verbose_name': 'zaproszenie do znajomych',
                'verbose_name_plural': 'zaproszenia do znajomych',
            },
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='correct_answer',
            field=models.CharField(verbose_name='poprawna odpowiedź', choices=[('a', 'Odpowiedź A'), ('b', 'Odpowiedź B'), ('c', 'Odpowiedź C'), ('d', 'Odpowiedź D')], max_length=1),
        ),
    ]
