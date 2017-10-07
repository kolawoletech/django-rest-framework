from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^todo/$', views.item_list),
    url(r'^todo/(?P<pk>[0-9]+)/$', views.item_detail),
]