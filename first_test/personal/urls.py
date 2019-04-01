
from . import views
from django.conf.urls import url, include

'''#call functions from view.py same directory'''

urlpatterns = [
   url(r'^home/', views.home, name='home'),
   url(r'^$', views.index, name='index'),

]
