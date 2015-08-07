# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0002_auto_20150807_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='comments',
            field=models.TextField(max_length=500, default=''),
        ),
    ]
