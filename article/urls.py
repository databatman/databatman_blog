
# coding: utf-8
from django.conf.urls import url

from . import views
from feeds import AllPostsRssFeed

app_name = 'article'
urlpatterns = [
    url(r'test', views.test, name='test'),
    url(r'home', views.home, name='home'),
    url(r'about', views.about, name='about'),
    url(r'rss', AllPostsRssFeed(), name='rss'),

    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]
