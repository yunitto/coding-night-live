# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-30 18:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_room', '0006_room_user_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='user_count',
        ),
    ]
