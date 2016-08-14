# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=10)),
                ('handout', models.FileField(upload_to='adminuploads/courses/handouts/')),
                ('image', models.ImageField(null=True, upload_to='adminuploads/courses/images/', blank=True)),
                ('category', models.CharField(max_length=50, choices=[('Electronics', 'Electronics'), ('Computer Science', 'Computer Science'), ('Mechanical', 'Mechanical'), ('Chemical', 'Chemical'), ('Graphics and Designing', 'Graphics and Designing')])),
                ('subcategory', models.CharField(max_length=50, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Mentors',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('course', models.ForeignKey(related_name='mentorcourse', to='course.Course')),
                ('mentor', models.ForeignKey(related_name='mentor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=150)),
                ('instr', tinymce.models.HTMLField()),
                ('upload', models.FileField(null=True, upload_to='adminuploads/courses/uploads/', blank=True)),
                ('course', models.ForeignKey(related_name='modulecourse', to='course.Course')),
            ],
        ),
    ]
