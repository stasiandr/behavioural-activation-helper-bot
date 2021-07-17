from django.urls import path, include
from rest_framework import routers

from .views import ActivityListCreate, SessionViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('activities', ActivityListCreate.as_view()),
    path('activities/start', SessionViewSet.as_view({'post': 'create'})),
    path('activities/<int:pk>/end/', SessionViewSet.as_view({'post': 'end_session'})),
    path('activities/<int:pk>/add/', SessionViewSet.as_view({'post': 'add_activity'})),
]
