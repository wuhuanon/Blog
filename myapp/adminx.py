import xadmin
from .models import *
from xadmin import views
from xadmin.layout import Fieldset
from xadmin.plugins.auth import UserAdmin
# 全局配置
class BaseSetting(object):
    #     主题
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    #左上角的字段
    site_title = "博客后台管理系统"
    # 底部字段
    site_footer = "个人博客"
    menu_style = "accordion"


class UseruAdmin(UserAdmin):
    pass
class ArticleAdmin(object):
    # 显示项
    list_display = ('title', 'desc', 'click_count')
    # 搜索字段
    search_fields = ('title', 'desc')
    #
    list_filter = ['user__username', 'title','desc', 'is_recommend', 'date_publish', 'category', 'tag']
    # 连接项
    list_display_links = ('title', 'desc',)
    # 可修改
    list_editable = ('click_count',)
    ordering = ['-date_publish']
    style_fields = {"content": "ueditor"}
    form_layout = (
        (
            Fieldset('基本信息', 'title', 'desc', 'content', 'user', 'category', 'tag'  ),
            Fieldset('高级设置','click_count', 'is_recommend')
        )
    )
    # fieldsets = (
    #             (None, {
    #                 'fields': ('title', 'desc', 'content', 'user', 'category', 'tag',)
    #             }),
    #             ('高级设置', {
    #                 'classes': ('collapse',),
    #                 'fields': ('click_count', 'is_recommend',)
    #             }),
    #         )

    # class Media:
    #     js = (
    #         '/static/js/kindeditor-4.1.10/kindeditor-min.js',
    #         '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
    #         '/static/js/kindeditor-4.1.10/config.js',
    #     )
xadmin.site.register(Tag)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Category)
xadmin.site.register(Comment)
xadmin.site.register(Links)
xadmin.site.register(Ad)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)