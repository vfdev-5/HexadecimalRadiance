# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name=b'Dataset name')),
                ('googlePlayUrl', models.URLField(verbose_name=b'Application url in Google Play Store')),
                ('appFile', models.FileField(upload_to=b'', verbose_name=b'Application apk file')),
            ],
        ),
    ]
