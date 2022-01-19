from django.urls import include, path
from rest_framework import routers
from .views import PersonViewSet


app_name = 'staff'

router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)


urlpatterns = [
    path('', include(router.urls)),
]