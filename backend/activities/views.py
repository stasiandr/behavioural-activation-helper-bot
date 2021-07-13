from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from activities.models import Activity
from activities.serializers import ActivitySerializer


class ActivityListCreate(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

