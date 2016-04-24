from django.conf.urls import url, include
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('dashboard/$', views.dashboard, name='dashboard'),
    url(r'^order/new/$', views.order_new, name='order_new'),
    url(r'^order/(?P<order_id>[0-9]+)/edit/$', views.order_edit, name='order_edit'),
    url(r'^(?P<order_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<order_id>[0-9]+)/drinks/$', views.drinks, name='drinks'),
    url(r'^(?P<order_id>[0-9]+)/placed/$', views.place_order, name='place_order'),
    url(r'^(?P<order_id>[0-9]+)/status/$', views.status, name='status'),
    url('^', include('django.contrib.auth.urls')),
    url('^register/$', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='/coffee'
    )),
]
