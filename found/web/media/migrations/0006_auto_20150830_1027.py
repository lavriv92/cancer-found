# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_auto_20150829_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
        ),
        migrations.RemoveField(
            model_name='galery',
            name='photos',
        ),
        migrations.DeleteModel(
            name='Galery',
        ),
        migrations.AddField(
            model_name='photo',
            name='group',
            field=models.ForeignKey(to='media.PhotoGroup', default=1, verbose_name='group'),
            preserve_default=False,
        ),
    ]
