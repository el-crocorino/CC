# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_trip_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='max_amount',
            new_name='amount_limit',
        ),
        migrations.AddField(
            model_name='trip',
            name='participants_limit',
            field=models.IntegerField(default=0),
        ),
    ]
