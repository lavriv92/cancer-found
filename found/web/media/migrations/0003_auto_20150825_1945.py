# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20150825_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galery',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='galery',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='object_id',
        ),
        migrations.AddField(
            model_name='galery',
            name='photos',
            field=models.ManyToManyField(db_constraint='photos', to='media.Photo'),
        ),
    ]
