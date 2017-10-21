from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)

# Debugging send_mail (python -m smtpd -n -c DebuggingServer localhost:1025)

urlpatterns = [
    url(r'^register/$', views.register, name='users.register'),
    url(r'^profile/$', views.profile, name='users.profile'),
    url(r'^login/$', login, { 'template_name': 'accounts/login.html' }, name='users.login'),
    url(r'^logout/$', logout, { 'template_name': 'accounts/logout.html' }, name='users.logout'),
    url(r'^profile/edit/$', views.edit_profile, name='users.edit_profile'),
    url(r'^profile/password/$', views.change_password, name='users.change_password'),
    url(r'^reset-password/$', password_reset, { 'template_name': 'accounts/reset_password.html', 'email_template_name': 'accounts/password_reset_email.html' }, name='users.password_reset'),
    url(r'^reset-password/done/$', password_reset_done, { 'template_name': 'accounts/password_reset_done.html' }, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, { 'template_name': 'accounts/password_reset_confirm.html' }, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, { 'template_name': 'accounts/password_reset_complete.html' }, name='password_reset_complete'),
]
