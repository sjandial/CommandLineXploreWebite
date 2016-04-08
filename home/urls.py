from django.conf.urls import include,url
from home import views
urlpatterns = [
    url(r'^(\d{1,20})/$',views.home_page,name='home_page'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^login/$', views.user_login, name='login'),
    url(r'^profile/$',views.user_profile,name='profile'),
    url(r'^submit_ans',views.submit_ans,name='submit_ans'),
    url(r'^logout/$',views.logout,name='logout'),
    ]