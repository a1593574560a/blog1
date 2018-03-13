#_*_ encoding: utf-8 _*_
__author__ = "Administrator"
__date__ = "2018/1/30 , 21:36"
from django.conf.urls import url,include
from article.views import IndexView,TitleDetailView,ArticleListView,SearchView
from .views import StudyListView,StudyDetailView,StudySearchView

from django.views.generic import TemplateView
from .views import ResourceSearchView
urlpatterns = [
    url(r'^article_detail/(?P<article_id>\d+)/$', TitleDetailView.as_view(), name='article_detail'),
    url(r'^article_list/$',ArticleListView.as_view(),name='article_list'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^study_list/$',StudyListView.as_view(),name='study_list'),
    url(r'^study_detail/(?P<study_id>\d+)/$', StudyDetailView.as_view(), name='study_detail'),
    url(r'^search_study/$', StudySearchView.as_view(), name='search_study'),
    url(r'^search_rss/$', ResourceSearchView.as_view(), name='search_rss'),

]



