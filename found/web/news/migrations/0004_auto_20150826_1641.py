# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_entry_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='main_image',
            field=models.ImageField(null=True, upload_to='news', verbose_name='main image'),
        ),
    ]
