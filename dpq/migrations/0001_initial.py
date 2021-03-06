# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-02 18:45
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.contrib.postgres.functions.TransactionNow)),
                ('execute_at', models.DateTimeField(default=django.contrib.postgres.functions.TransactionNow)),
                ('priority', models.PositiveIntegerField(default=0, help_text='Jobs with higher priority will be processed first.')),
                ('task', models.CharField(max_length=255)),
                ('args', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.AddIndex(
            model_name='job',
            index=models.Index(fields=['-priority', 'created_at'], name='dpq_job_priorit_aa4927_idx'),
        ),
    ]
