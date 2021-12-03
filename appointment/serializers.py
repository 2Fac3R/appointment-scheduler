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


class DatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date']
    