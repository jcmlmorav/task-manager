from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='tasks.index'),
    url(r'^manage/$', views.manage, name='tasks.manage')
]
