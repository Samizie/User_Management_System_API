from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("users/", views.UserManView.as_view(), name='list_users'),
    path("user/create/", views.UserManView.as_view(), name='create_user'),
    re_path(r'^user/(?P<input>(\d+|[a-zA-Z]+))/$', views.UserGetView.as_view(), name='get_user'),
    re_path(r'^user/update/(?P<input>(\d+|[a-zA-Z]+))/$', views.UserGetView.as_view(), name='update_user'),
    re_path(r'^user/delete/(?P<input>(\d+|[a-zA-Z]+))/$', views.UserGetView.as_view(), name='delete_user'),
    
]
