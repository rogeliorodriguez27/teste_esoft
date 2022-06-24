from django.conf.urls import url, include
from . import views

app_name = 'products'

urlpatterns = [
    url(r'^products/$', views.products_list, name='products_list'),
    url(r'^products/create$', views.products_create, name='product_create'),
    url(r'^products/(?P<id>\d+)/update$', views.product_update, name='product_update'),
    url(r'^products/(?P<id>\d+)/delete$', views.product_delete, name='product_delete'),
]