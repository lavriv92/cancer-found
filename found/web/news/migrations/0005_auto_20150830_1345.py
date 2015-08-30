# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150826_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_anouns',
            field=models.BooleanField(verbose_name='is anouns', default=False),
        ),
        migrations.AddField(
            model_name='entry',
            name='is_recomended',
            field=models.BooleanField(verbose_name='is recomended', default=False),
        ),
    ]
