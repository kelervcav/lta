# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20180320_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='order_by',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
