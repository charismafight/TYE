# Generated by Django 2.1.7 on 2019-06-10 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TYE', '0003_auto_20190610_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='img',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='照片'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 0, 45, 13, 189359), verbose_name='发布时间'),
        ),
    ]