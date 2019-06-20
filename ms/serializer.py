from rest_framework import serializers
from .models import Profile,Schedule

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','bio','dp','user')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id','title', 'time','description', )        