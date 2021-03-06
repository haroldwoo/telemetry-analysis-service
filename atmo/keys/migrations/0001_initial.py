# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.
# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-13 15:37
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SSHKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='Name to give to this public key', max_length=100)),
                ('key', models.TextField(help_text='Should start with one of the following prefixes: ssh-rsa, ssh-dss, ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, ecdsa-sha2-nistp521')),
                ('fingerprint', models.CharField(blank=True, max_length=48, unique=True)),
                ('created_by', models.ForeignKey(help_text='User that created the instance.', on_delete=django.db.models.deletion.CASCADE, related_name='created_sshkeys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('view_sshkey', 'Can view SSH key')],
            },
        ),
    ]
