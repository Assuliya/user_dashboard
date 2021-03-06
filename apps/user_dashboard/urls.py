from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'user/login$', views.login, name='login'),
    url(r'user/register$', views.register, name='register'),
    url(r'user/(?P<user_id>\d+)/edit$', views.edit, name='edit'),
    url(r'user/dashboard$', views.dashboard, name='dashboard'),
    url(r'^user/(?P<user_id>\d+)$', views.show, name='show'),
    url(r'user/deletion_page$', views.deletion_page, name='deletion_page'),

    url(r'^user/login_process$', views.login_process, name='login_process'),
    url(r'^user/register_process$', views.register_process, name='register_process'),
    url(r'user/(?P<user_id>\d+)/update$', views.update, name='update'),
    url(r'user/(?P<user_id>\d+)/update_pass$', views.update_pass, name='update_pass'),
    url(r'^user/logout$', views.logout, name='logout'),
    url(r'^user/(?P<user_id>\d+)/delete$', views.delete, name='delete'),

    url(r'^user/(?P<page_id>\d+)/add_message$', views.add_message, name='add_message'),
    url(r'^user/(?P<message_id>\d+)/add_comment$', views.add_comment, name='add_comment')

]
