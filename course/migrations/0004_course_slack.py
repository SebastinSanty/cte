# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20160817_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slack',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
