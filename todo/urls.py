from django.conf.urls import url, include
from todo import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'todo', views.ItemViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]



