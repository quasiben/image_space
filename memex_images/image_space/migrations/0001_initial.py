# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_file_name', models.CharField(max_length=200)),
                ('EXIF_LensSerialNumber', models.CharField(max_length=200)),
                ('MakerNote_SerialNumberFormat', models.CharField(max_length=200)),
                ('EXIF_BodySerialNumber', models.CharField(max_length=200)),
                ('MakerNote_InternalSerialNumber', models.CharField(max_length=200)),
                ('MakerNote_SerialNumber', models.CharField(max_length=200)),
                ('Image_BodySerialNumber', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
