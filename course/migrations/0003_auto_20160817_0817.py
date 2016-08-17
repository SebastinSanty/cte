# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_auto_20160814_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('course', models.ForeignKey(to='course.Course', related_name='studentcourse')),
                ('student', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='coursestudent')),
            ],
        ),
        migrations.AlterField(
            model_name='mentors',
            name='mentor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='coursementor'),
        ),
    ]
