# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20170805_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'refused'), (1, 'pending'), (2, 'accepted'), (3, 'running'), (4, 'honored')], default=1),
        ),
    ]