# Generated by Django 2.1.7 on 2020-01-11 14:46

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('TYE', '0010_auto_20191221_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cname', models.CharField(max_length=30, verbose_name='中文名称')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='archive',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='video', verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 22, 46, 3, 820526), verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 22, 46, 3, 821526), verbose_name='发布时间'),
        ),
    ]