# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 19:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_auto_20170905_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 19, 26, 57, 608535, tzinfo=utc), verbose_name='date published'),
        ),
    ]
