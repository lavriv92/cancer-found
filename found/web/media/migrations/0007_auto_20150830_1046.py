# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_auto_20150830_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('video', models.FileField(upload_to='videos', verbose_name='video')),
                ('created', models.DateTimeField(verbose_name='created', auto_now=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'video',
            },
        ),
        migrations.CreateModel(
            name='VideoGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
            ],
            options={
                'verbose_name': 'video group',
                'verbose_name_plural': 'video groups',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='group',
            field=models.ForeignKey(verbose_name='video group', to='media.VideoGroup'),
        ),
    ]
