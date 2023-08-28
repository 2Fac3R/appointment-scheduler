from django.conf import settings

from django.contrib.auth.models import User
from django.db import models


class Appointment(models.Model):
    """Model representing an appointment"""
    date = models.DateTimeField(null=False, blank=False)
    user = models.ManyToManyField(User)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.date.strftime(settings.DATE_TIME_FIELD_FORMAT))
