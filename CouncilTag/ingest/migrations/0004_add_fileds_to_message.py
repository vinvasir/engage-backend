# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-06 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0003_nullable-integer-opinion'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='authcode',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='business_owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='child_school',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='home_owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='resident',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='school',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='works',
            field=models.BooleanField(default=False),
        ),
    ]
