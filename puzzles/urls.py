from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^puzzles/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),
]

