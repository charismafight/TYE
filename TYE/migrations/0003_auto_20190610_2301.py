# Generated by Django 2.1.7 on 2019-06-10 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TYE', '0002_auto_20190609_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 10, 23, 1, 41, 948692), verbose_name='发布时间'),
        ),
    ]
