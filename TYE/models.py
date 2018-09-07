from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='uploads/')


class Archive(models.Model):
    title = models.TextField('标题', max_length=100)
    description = models.TextField('描述', max_length=2000)
    votes = models.IntegerField('投票数', default=0)
    file = models.FileField('文件', default=None, storage=fs)
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):
        return self.title
