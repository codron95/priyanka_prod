# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.ImageField(default='0', upload_to='posts/'),
        ),
    ]
