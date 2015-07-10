# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150710_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('question', models.CharField(verbose_name='Pytanie', max_length=200)),
                ('answer_a', models.CharField(verbose_name='Odpowiedź A', max_length=200)),
                ('answer_b', models.CharField(verbose_name='Odpowiedź B', max_length=200)),
                ('answer_c', models.CharField(verbose_name='Odpowiedź C', max_length=200)),
                ('answer_d', models.CharField(verbose_name='Odpowiedź D', max_length=200)),
                ('correct_answer', models.CharField(choices=[('a', 'Odpowiedź A'), ('b', 'Odpowiedź B'), ('c', 'Odpowiedź C'), ('d', 'Odpowiedź D')], max_length=1)),
            ],
        ),
    ]
