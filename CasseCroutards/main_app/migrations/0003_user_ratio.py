# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20170726_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ratio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
