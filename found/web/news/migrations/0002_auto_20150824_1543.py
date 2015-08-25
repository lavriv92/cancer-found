# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='project',
            field=models.ForeignKey(null=True, to='projects.Project', verbose_name='project'),
        ),
    ]
