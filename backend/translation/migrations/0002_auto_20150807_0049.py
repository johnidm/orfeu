# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('phrase', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=100)),
                ('comments', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, populate_from='name', editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='sentence',
            name='translate_from',
            field=models.ForeignKey(related_name='translate_from', to='translation.Language'),
        ),
        migrations.AddField(
            model_name='sentence',
            name='translate_to',
            field=models.ForeignKey(related_name='translate_to', to='translation.Language'),
        ),
    ]
