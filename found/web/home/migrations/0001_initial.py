# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memeber',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('photo', models.ImageField(verbose_name='photo', upload_to='members')),
                ('first_name', models.CharField(verbose_name='first name', max_length=255)),
                ('last_name', models.CharField(verbose_name='last name', max_length=255)),
                ('position', models.CharField(verbose_name='position', max_length=255)),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
        ),
        migrations.CreateModel(
            name='MemeberGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
        ),
    ]
