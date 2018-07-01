# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_auto_20160630_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, default='This will be auto-generated', max_length=100),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_type',
            field=models.CharField(choices=[('people', 'People'), ('nature', 'Nature'), ('bnw', 'Black & White')], default='people', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('published', 'Published'), ('stories', 'Stories'), ('travelogue', 'Travelogue')], default='published', max_length=20),
        ),
    ]