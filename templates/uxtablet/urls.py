from django.conf.urls import url
from uxtablet import views

urlpatterns = [
    url(r'^$', views.home, name='hello'),
    url(r'^companies', views.companies, name='companies'),
    url(r'^connect',views.connect, name='connect'),
    url(r'^user/(?P<user_id>\d+)/$',views.insertion_dechet, name='insertion_dechet'),
    url(r'^user/(?P<user_id>\d+)/(?P<prediction>\d+)/$', views.plastic, name='plastic'),
    #url(r'^user/(?P<user_id>\d+)/(?P<plastic_id>\d+)/your_waste$', views.your_waste, name='your_waste'),
    url(r'^user/(?P<user_id>\d+)/(?P<plastic_id>\d+)/printsomelove$', views.print_some_love, name='print_some_love'),
    url(r'^user/(?P<user_id>\d+)/seeyou$', views.see_you, name='see_you')
    ]
