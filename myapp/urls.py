from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from myapp.upload import upload_image
from . import views
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r"^media/(?P<path>.*)$",serve,{"document_root": settings.MEDIA_ROOT,}),
    url(r'^xadmin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^image/upload/$', views.UploadImageView.as_view(), name='image_upload'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^article/$', views.article, name='article'),
    url(r'^comment/post/$', views.comment_post, name='comment_post'),
    url(r'^logout/$', views.do_logout, name='logout'),
    url(r'^reg/$', views.do_reg, name='reg'),
    url(r'^login/', views.do_login, name='login'),
    url(r'^category/$', views.category, name='category'),
    url(r'^tag/$', views.tag, name='tag'),
]