# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 1, 17, 46, 39, 426338)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lst',
            field=models.IntegerField(default=0),
        ),
    ]
