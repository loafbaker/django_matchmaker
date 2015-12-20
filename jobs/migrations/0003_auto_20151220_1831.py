# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20151213_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='slug',
            field=models.SlugField(default='abc-2015-12-20-18-31-13-220154-00-00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(default='abc-2015-12-20-18-31-29-031324-00-00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(default='abc-2015-12-20-18-31-31-405138-00-00'),
            preserve_default=False,
        ),
    ]
