# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('report_file', models.FileField(verbose_name='file', upload_to='reports')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
            ],
            options={
                'verbose_name': 'report',
                'verbose_name_plural': 'reports',
            },
        ),
    ]
