from django.conf.urls import url
from humans_of_hive import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^(?P<post_name_slug>[\w\-]+)/$', views.show_post, name='show_post'),
    url(r'^(?P<post_name_slug>[\w\-]+)/add_comment/$', views.add_comment, name='add_comment'),

    #how to access?
    url(r'^USER_PROFILE/$', views.show_profile, name='user_profile'),
    url(r'^USER_PROFILE/USER_POSTS/$', views.user_posts, name='user_posts'),

    url(r'^hall_of_fame/$', views.hall_of_fame, name='hall_of_fame'),
]
