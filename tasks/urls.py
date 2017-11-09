from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='tasks.index'),
    url(r'^home/$', views.home, name='tasks.home'),
    url(r'^projects/$', views.projects, name='tasks.projects'),
    url(r'^projects/new/$', views.projects_new, name='tasks.projects_new'),
    url(r'^projects/(?P<slug>[\w-]+)/$', views.projects_view, name='tasks.projects_view')
]
