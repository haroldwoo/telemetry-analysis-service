# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-04-26 09:39
from __future__ import unicode_literals

from django.db import migrations


def fix_usernames(apps, schema_editor):
    pass


def revert_usernames(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial_site'),
    ]

    operations = [
        migrations.RunPython(
            fix_usernames,
            revert_usernames,
        ),
    ]
