# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0018_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f101',
            name='updated_at',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='f201',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 18, 4, 30, 38, 138847), editable=False),
        ),
    ]
