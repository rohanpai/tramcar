# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0009_auto_20161006_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='protocol',
            field=models.CharField(choices=[('http', 'http'), ('https', 'https')], default='http', help_text='The protocol to use when building links in e-mail templates, etc.', max_length=5),
        ),
    ]
