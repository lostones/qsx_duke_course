# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20170302_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='u_type',
        ),
        migrations.AddField(
            model_name='user',
            name='u_email',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
