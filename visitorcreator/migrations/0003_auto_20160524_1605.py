# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 16:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitorcreator', '0002_auto_20160524_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='visitor',
            name='visitor_type',
            field=models.CharField(default='new', max_length=20),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='company_to_visit',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='email',
            field=models.CharField(max_length=255, validators=[django.core.validators.EmailValidator]),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='employee_to_visit',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
