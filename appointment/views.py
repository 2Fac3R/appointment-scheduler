from rest_framework import viewsets, generics
from rest_framework import permissions
from django.contrib.auth.models import User, Group

from .serializers import UserSerializer, GroupSerializer, AppointmentSerializer, DatesSerializer
from .models import Appointment


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows appointments to be viewed or edited.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AppointmentList(generics.ListAPIView):
    """
    API endpoint that shows appointments filtered by User id
    """
    serializer_class = DatesSerializer

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.query_params.get('id', None))
