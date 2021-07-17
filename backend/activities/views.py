from django.shortcuts import render
from rest_framework import generics, viewsets

# Create your views here.
from rest_framework.response import Response

from activities.models import Activity, Session
from activities.serializers import ActivitySerializer, SessionSerializer


class ActivityListCreate(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def end_session(self, request, pk=None):
        s = Session.objects.get(id=pk)
        s.end_activity()
        serializer = SessionSerializer(s)
        return Response(serializer.data)

    def add_activity(self, request, pk=None):
        s = Session.objects.get(id=int(pk))

        name = request.data['name']
        score = request.data['score']

        act = Activity(name=name, score=score)
        act.save()
        s.add_activity(act)
        serializer = SessionSerializer(s)
        return Response(serializer.data)





