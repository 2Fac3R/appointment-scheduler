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

    def is_half_or_hour(time):
        """
        Check if minute is an hour or half-hour.
        """
        valid = [00, 30]
        if time.minute not in valid:
            raise serializers.ValidationError(
                "All appointments must start and end on the hour or half-hour.")
        return time

    date = serializers.DateTimeField(
        format=settings.DATE_TIME_FIELD_FORMAT,
        validators=[is_half_or_hour]
    )


class DatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date']
    date = serializers.DateTimeField(format=settings.DATE_TIME_FIELD_FORMAT)
