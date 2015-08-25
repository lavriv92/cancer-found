# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galery',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='gallery',
        ),
        migrations.AddField(
            model_name='galery',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='galery',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.FileField(upload_to='static/uploads', verbose_name='image'),
        ),
    ]
