# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-08 13:32
from django.db import migrations

from atmo.models import PermissionMigrator


def assign_spark_job_view_permission(apps, schema_editor):
    SparkJob = apps.get_model('jobs', 'SparkJob')
    PermissionMigrator(apps, SparkJob, 'view', user_field='created_by').assign()


def remove_spark_job_view_permission(apps, schema_editor):
    SparkJob = apps.get_model('jobs', 'SparkJob')
    PermissionMigrator(apps, SparkJob, 'view', user_field='created_by').remove()


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20161108_0933'),
        ('auth', '0007_alter_validators_add_error_messages'),
        ('guardian', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            assign_spark_job_view_permission,
            remove_spark_job_view_permission,
        ),
    ]
