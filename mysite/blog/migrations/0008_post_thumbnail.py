# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-30 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180414_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='bj.jpg', editable=False, upload_to='thumbs/'),
            preserve_default=False,
        ),
    ]
