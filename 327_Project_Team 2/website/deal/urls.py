from django.conf.urls import url, include
from . import views
from django.urls import path

app_name = 'deal'

#deal/
urlpatterns = {
    path('', views.index, name='index'),
    path('apparels/', views.apparels, name='apparels'),
    path('accessories/', views.accessories, name='accessories'),
    path('services/', views.services, name='services'),
    path('electronics/', views.electronics, name='electronics'),
    path('dailyessentials/', views.dailyessentials, name='dailyessentials'),
    path('food/', views.food, name='food'),
    path('all/', views.alldeals, name='alldeals'),
    url(r'^(?P<deal_id>[0-9]+)/$', views.detail, name='detail'),
    path('add/', views.DealCreate.as_view(), name='deal-add')
}
