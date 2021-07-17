from rest_framework import serializers

from activities.models import Activity, Session


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ['id', 'name', 'type', 'score', 'end_date']


class SessionSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        obj = Session.objects.create(**validated_data)
        obj.start_activity()
        obj.save()
        return obj

    class Meta:
        model = Session
        fields = ['id', 'activities']
