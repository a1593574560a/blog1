# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-09 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_banner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='banner',
            name='image2',
            field=models.ImageField(default='', max_length=200, upload_to=b'', verbose_name='\u8f6e\u64ad\u56fe'),
        ),
    ]
