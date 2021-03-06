# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_order_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='near_misses',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='no_light',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='rider_dismount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='speed_limit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='weaving',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='wrong_path',
            field=models.BooleanField(default=False),
        ),
    ]
