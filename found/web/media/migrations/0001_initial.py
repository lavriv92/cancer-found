# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150824_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
                ('entry', models.ForeignKey(to='news.Entry', verbose_name='entry')),
            ],
            options={
                'verbose_name_plural': 'galeries',
                'verbose_name': 'galery',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('image', models.FileField(verbose_name='image', upload_to='')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
                ('entry', models.ForeignKey(null=True, to='news.Entry', verbose_name='entry')),
                ('gallery', models.ForeignKey(null=True, to='media.Galery', verbose_name='galery')),
            ],
            options={
                'verbose_name': 'photo',
            },
        ),
    ]
