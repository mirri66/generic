from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^puzzles/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^postlogin$', views.postlogin, name='postlogin'),
    url(r'^pay$', views.pay_view, name='pay'),
    url(r'^postpay$', views.postpay, name='postpay'),
    url(r'^logout$','django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'),
    url(r'^signup$', views.signup, name='signup'),
]

