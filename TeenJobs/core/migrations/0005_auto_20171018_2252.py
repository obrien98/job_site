# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-18 22:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_employer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='last_name',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
