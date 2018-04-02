from django.conf.urls import url
from . import views

#deal/
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all/', views.alldeals, name='alldeals'),
    url(r'^(?P<deal_id>[0-9]+)/$', views.detail, name='detail'),

]
