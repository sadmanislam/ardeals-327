from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'deal'

#deal/
urlpatterns = {
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    # url(r'^all/', views.alldeals, name='alldeals'),
    path('all/', views.alldeals, name='alldeals'),
    path('apparels/', views.apparels, name='apparels'),
    #path('accessories/', views.accessories, name='accessories'),
    #path('services/', views.services, name='services'),
    #path('electronics/', views.electronics, name='electronics'),
    #path('dailyessentials/', views.dailyessentials, name='dailyessentials'),
    #path('food/', views.food, name='food'),


    url(r'^(?P<deal_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),

}
