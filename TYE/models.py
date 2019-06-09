from django.db import models
from datetime import datetime


class Archive(models.Model):
    title = models.TextField('标题', max_length=100)
    description = models.TextField('描述', max_length=2000, null=True)
    votes = models.IntegerField('投票数', default=0, editable=False)
    file = models.FileField('文件', default=None, null=True)
    img = models.ImageField('图片', null=True)
    pub_date = models.DateTimeField('发布时间', default=datetime.now())
    days_of_born = models.IntegerField('出生天数', editable=False)

    def get_days_of_born(self):
        self.days_of_born = (self.pub_date - datetime(2018, 2, 8)).days
        return

    def __str__(self):
        return self.title
