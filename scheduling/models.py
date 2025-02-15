from django.db import models
from account.models import User

from django.utils.translation import gettext_lazy as _
# Create your models here.

class Availability(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availabilities")
    day_of_week = models.IntegerField(choices=[(0, _("Saturday")), (1, _("Sunday")), (2, _("Monday")), (3, _("Tuesday")), (4, _("Wednesday")), (5, _("Thursday")), (6, _("Friday"))])
    start_time = models.TimeField()
    end_time = models.TimeField()

