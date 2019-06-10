from django.db import models
from datetime import datetime, timezone, timedelta
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Transpose, SmartResize


class Archive(models.Model):
    title = models.TextField('标题', max_length=100)
    description = models.TextField('描述', max_length=2000, null=True, blank=True)
    votes = models.IntegerField('投票数', default=0, editable=False)
    file = models.FileField('文件', default=None, null=True, blank=True)
    img = models.ImageField('图片', null=True)
    img_thumbnail = ImageSpecField(
        source='img',
        processors=[Transpose(), SmartResize(200, 200)],
        format='JPEG',
        options={'quality': 75}
    )
    pub_date = models.DateTimeField('发布时间', default=datetime.now())
    days_of_born = models.IntegerField('出生天数', editable=False)

    def get_days_of_born(self):
        born = datetime(2018, 2, 8, tzinfo=timezone(timedelta(hours=8)))
        self.days_of_born = (self.pub_date - born).days
        return

    def __str__(self):
        return self.title
