# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 19:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0007_auto_20170905_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 5, 19, 38, 8, 617565, tzinfo=utc), verbose_name='date published'),
        ),
    ]
