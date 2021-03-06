# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 16:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laverie', '0003_auto_20160512_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appareil',
            name='temps_restant',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='appareil',
            name='type',
            field=models.CharField(choices=[('machine', 'Machine à laver'), ('seche_linge', 'Sèche linge')], default='machine', max_length=20),
        ),
    ]
