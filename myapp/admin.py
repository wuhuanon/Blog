from django.contrib import admin
from .models import *
# Register your models here.

# class Articleadmin(admin.ModelAdmin):
#     # 显示项
#     list_display = ('title', 'desc', 'click_count',)
#     # 连接项
#     list_display_links = ('title', 'desc',)
#     # 可修改
#     list_editable = ('click_count',)
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'desc', 'content', 'user', 'category', 'tag',)
#         }),
#         ('高级设置', {
#             'classes': ('collapse',),
#             'fields': ('click_count', 'is_recommend',)
#         }),
#     )
#     class Media:
#         js = (
#             '/static/js/kindeditor-4.1.10/kindeditor-min.js',
#             '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
#             '/static/js/kindeditor-4.1.10/config.js',
#         )
# admin.site.register(User)
# admin.site.register(Tag)
# admin.site.register(Article, Articleadmin)
# admin.site.register(Category)
# admin.site.register(Comment)
# admin.site.register(Links)
# admin.site.register(Ad)