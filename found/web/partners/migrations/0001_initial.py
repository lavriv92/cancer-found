# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('logo', models.ImageField(verbose_name='logo', upload_to='partners')),
                ('url', models.URLField(verbose_name='url')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
            ],
            options={
                'verbose_name': 'partner',
            },
        ),
    ]
