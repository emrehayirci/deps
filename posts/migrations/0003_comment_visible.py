# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-02 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170831_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
