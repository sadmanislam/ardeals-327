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
    path('add/', views.DealCreate.as_view(), name='deal-add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.DealUpdate.as_view(), name='deal-update'),
    url(r'^edit/(?P<pk>[0-9]+)/delete/$', views.DealDelete.as_view(), name='deal-delete'),
    path('bcity/', views.bcity, name='bcity'),
    path('tejgaon/', views.tejgaon, name='tejgaon'),
    path('pd/', views.pd, name='pd'),
    path('mirpur/', views.mirpur, name='mirpur'),
    path('dhanmondi/', views.dhanmondi, name='dhanmondi'),
    path('uttara/', views.uttara, name='uttara'),
    path('lalmatia/', views.lalmatia, name='lalmatia'),
    path('moghbazar/', views.moghbazar, name='moghbazar'),
    path('banani/', views.banani, name='banani'),
    path('g1/', views.g1, name='g1'),
    path('g2/', views.g2, name='g2'),

}
