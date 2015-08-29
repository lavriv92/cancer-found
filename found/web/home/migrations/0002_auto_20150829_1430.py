# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('doc_file', models.FileField(verbose_name='doc_file', upload_to='files')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'documents',
                'verbose_name': 'document',
            },
        ),
        migrations.CreateModel(
            name='VolonteerTask',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'tasks',
                'verbose_name': 'task',
            },
        ),
        migrations.AddField(
            model_name='memeber',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created', default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='memeber',
            name='updated',
            field=models.DateTimeField(verbose_name='updated', auto_now=True, default=timezone.now()),
            preserve_default=False,
        ),
    ]
