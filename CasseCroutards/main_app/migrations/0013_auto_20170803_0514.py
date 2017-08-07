# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(-1, 'Refused'), (0, 'Pending'), (1, 'Accepted'), (2, 'Running'), (3, 'Honored')], default=0),
        ),
    ]