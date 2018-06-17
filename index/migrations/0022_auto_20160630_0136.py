# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_auto_20160621_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_type',
            field=models.CharField(choices=[('people', 'People'), ('landscape', 'Landscape'), ('architecture', 'Architecture')], default='people', max_length=20),
        ),
    ]
