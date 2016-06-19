# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 18:52
from __future__ import unicode_literals

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_auto_20160601_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='selected_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='No Content'),
        ),
    ]
