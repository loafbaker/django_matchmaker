# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='text',
            field=models.CharField(unique=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(unique=True, max_length=250),
        ),
        migrations.AlterUniqueTogether(
            name='employer',
            unique_together=set([('name', 'location')]),
        ),
    ]
