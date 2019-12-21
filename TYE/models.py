import os

from django.db import models
from datetime import datetime, timezone, timedelta
from imagekit.models import ImageSpecField
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.processors import ResizeToFill, Transpose, SmartResize, Thumbnail

from TYE.image_tools import rotate_image


class Archive(models.Model):
    title = models.TextField('标题', max_length=100)
    description = models.TextField('描述', max_length=2000, null=True, blank=True)
    votes = models.IntegerField('投票数', default=0, editable=False)
    file = models.FileField('文件', default=None, null=True, blank=True)
    img = models.ImageField('照片', upload_to='img', max_length=255, blank=True, null=True)
    img_thumbnail = ImageSpecField(source='img',
                                   processors=[ResizeToFill(100, 50)],
                                   format='JPEG',
                                   options={'quality': 60})
    pub_date = models.DateTimeField('发布时间', default=datetime.now())
    days_of_born = models.IntegerField('出生天数', editable=False)

    def get_days_of_born(self):
        born = datetime(2018, 2, 8, tzinfo=timezone(timedelta(hours=8)))
        self.days_of_born = (self.pub_date - born).days
        return

    def __str__(self):
        return self.title


@receiver(post_save, sender=Archive, dispatch_uid="update_image_archive")
def update_time(sender, instance, **kwargs):
    if instance.img:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fullpath = BASE_DIR + instance.img.url
        rotate_image(fullpath)


class Video(models.Model):
    title = models.TextField('标题', max_length=100)
    description = models.TextField('描述', max_length=2000, null=True, blank=True)
    votes = models.IntegerField('投票数', default=0, editable=False)
    file = models.FileField('文件', default=None, null=True, blank=True)
    pub_date = models.DateTimeField('发布时间', default=datetime.now())
    days_of_born = models.IntegerField('出生天数', editable=False)

    def get_days_of_born(self):
        born = datetime(2018, 2, 8, tzinfo=timezone(timedelta(hours=8)))
        self.days_of_born = (self.pub_date - born).days
        return

    def __str__(self):
        return self.title
