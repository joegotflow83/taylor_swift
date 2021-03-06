# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160223_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='favorite_album',
            field=models.CharField(blank=True, default='test', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='favorite_song',
            field=models.CharField(blank=True, default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
