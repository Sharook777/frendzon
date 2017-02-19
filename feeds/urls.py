
from django.conf.urls import url
from . import views
from comment.views import comment,delete_comment

urlpatterns = [
    url(r'^$', views.list_post, name="list"),
    url(r'^chat/$', views.chats, name="chat"),
    url(r'^create/$', views.create_post, name='create'),
    url(r'^(?P<id>\w+)/$', views.detail_post, name="detail"),
    url(r'^(?P<id>\w+)/update/$', views.update_post, name="update"),
    url(r'^(?P<id>\w+)/delete/$', views.delete_post, name="delete"),
    url(r'^(?P<post_id>\w+)/like/$', views.likes, name="like"),
    url(r'^(?P<id>\w+)/comment/$', comment, name="comment"),
    url(r'^delete/(?P<id>\w+)/comment/$', delete_comment, name="comment_del"),
]
