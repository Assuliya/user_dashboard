from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'user/login$', views.login, name='login'),
    url(r'user/register$', views.register, name='register'),
    url(r'user/edit$', views.edit, name='edit'),
    url(r'user/dashboard$', views.dashboard, name='dashboard'),
    # url(r'delete/(?P<user_id>\d+)$', delete, name='log_delete')
]
