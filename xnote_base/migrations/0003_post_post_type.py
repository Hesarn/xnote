# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xnote_base', '0002_auto_20160225_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('quick', 'Quick')], default='normal', max_length=50),
        ),
    ]
