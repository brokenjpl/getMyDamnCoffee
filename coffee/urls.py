from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
        url(r'^(?P<order_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^(?P<order_id>[0-9]+)/drinks/$', views.drinks, name='drinks'),
        url(r'^(?P<order_id>[0-9]+)/placed/$', views.place_order, name='place_order'),
        url(r'^(?P<order_id>[0-9]+)/status/$', views.status, name='status'),
]	
