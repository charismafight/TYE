# Generated by Django 2.1.7 on 2019-11-27 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TYE', '0008_auto_20190611_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 28, 1, 18, 40, 973050), verbose_name='发布时间'),
        ),
    ]
