# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-24 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_room', '0002_auto_20170123_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('md_blob', models.TextField()),
                ('now_id', models.AutoField(primary_key=True, serialize=False)),
                ('prev_id', models.PositiveSmallIntegerField()),
                ('next_id', models.PositiveSmallIntegerField()),
            ],
        ),
    ]