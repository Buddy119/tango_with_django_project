# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20170319_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=40),
        ),
    ]