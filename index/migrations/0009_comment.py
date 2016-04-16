# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-09 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20160409_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=20)),
                ('content', models.TextField(default='no-content')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.post')),
            ],
        ),
    ]