from django.conf import settings
from rest_framework import serializers

from django.contrib.auth.models import User, Group
from appointment.models import Appointment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['url', 'date', 'user']
    date = serializers.DateTimeField(format=settings.DATE_TIME_FIELD_FORMAT)


class DatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date']
    date = serializers.DateTimeField(format=settings.DATE_TIME_FIELD_FORMAT)