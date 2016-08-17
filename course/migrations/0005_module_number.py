# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_slack'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
