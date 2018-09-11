from django.db import models
from datetime import datetime


class Archive(models.Model):
    title = models.TextField('标题', max_length=100)
    description = models.TextField('描述', max_length=2000, null=True)
    votes = models.IntegerField('投票数', default=0)
    file = models.FileField('文件', default=None)
    pub_date = models.DateTimeField('发布时间', default=datetime.now())
    days_of_born = datetime(year=2018, month=2, day=8) - pub_date.time

    def __str__(self):
        return self.title
