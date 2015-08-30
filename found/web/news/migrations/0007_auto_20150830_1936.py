# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20150830_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='project',
            field=models.ForeignKey(null=True, to='projects.Project', blank=True, related_name='entries', verbose_name='project'),
        ),
    ]
