# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150824_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='main_image',
            field=models.FileField(upload_to='news', verbose_name='main image', null=True),
        ),
    ]
