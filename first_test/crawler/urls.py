
from . import views
from django.conf.urls import url, include

'''#call functions from views.py same directory'''

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^crawler/$', views.crawler, name='crawler'),
   url(r'^news/$', views.news, name='news'),
   url(r'^home/$', views.home, name='home'),

   #url(r'', views.news_from_db, name='news_from_db'),

]

