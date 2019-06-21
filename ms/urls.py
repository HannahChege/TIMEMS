from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^newprofile/', views.new_profile, name='new_profile'),
    url(r'^new/schedule/$', views.new_schedule, name='new-schedule'),
    # url(r'^api/schedule/$', views.ScheduleList.as_view()),
    # url(r'^api/profile/$', views.ProfileList.as_view()),
    # # url(r'api/schedule/schedule-id/(?P<pk>[0-9]+)/$',views.ScheduleDescription.as_view()),
    # url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
]
