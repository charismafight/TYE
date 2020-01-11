from django.contrib import admin
from .models import *


# Register your models here.
class ArchiveAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.get_days_of_born()
        super().save_model(request, obj, form, change)


class UserProfileAdmin(admin.ModelAdmin):
    # 定义admin总览里每行的显示信息
    list_display = ('cname', 'username', 'email')
    # 定义搜索框以哪些字段可以搜索
    search_fields = ('cname', 'username')


# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.get_days_of_born()
        super().save_model(request, obj, form, change)


admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Video, VideoAdmin)
# 引用的固定格式，注册的model和对应的Admin，Admin放在后边
# 同样还有noregister方法：比如admin.site.noregister(Group)，把group这个表在admin中去掉（默认user和group都是注册到admin中的）
admin.site.register(UserProfile, UserProfileAdmin)
