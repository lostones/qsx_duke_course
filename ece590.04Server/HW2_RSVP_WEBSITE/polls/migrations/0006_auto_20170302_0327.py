# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 03:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20170302_0208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pri_answer',
            old_name='answer',
            new_name='a',
        ),
        migrations.RenameField(
            model_name='pri_answer',
            old_name='user',
            new_name='u',
        ),
        migrations.RenameField(
            model_name='pri_event',
            old_name='event',
            new_name='e',
        ),
        migrations.RenameField(
            model_name='pri_event',
            old_name='user',
            new_name='u',
        ),
    ]
