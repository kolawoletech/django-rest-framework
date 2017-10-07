from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^todo/$',
        views.ItemList.as_view(),
        name='item-list'),
    url(r'^todo/(?P<pk>[0-9]+)/$',
        views.ItemDetail.as_view(),
        name='item-detail'),
    url(r'^todo/(?P<pk>[0-9]+)/highlight/$',
        views.ItemHighlight.as_view(),
        name='item-highlight'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]