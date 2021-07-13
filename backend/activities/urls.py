from django.urls import path, include
from rest_framework import routers
from .views import ActivityListCreate

router = routers.DefaultRouter()
# router.register(r'activities', ActivityListCreate)

urlpatterns = [
    path('', include(router.urls)),
    path('activities', ActivityListCreate.as_view())
]
