# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-13 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnUrl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anasurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='anasurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
