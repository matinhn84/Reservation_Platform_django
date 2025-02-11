from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# choices
OPTIOS_FOR_APPOINTMENT_STATUS = [
    ('P' , 'Pending'),
    ('C' , 'Confirmed'),
    ('R' , 'Rejected')
]
# models
class BookingSalon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("کاربر"))
    service = 1
    def save():
        date = 1
        pass

    status = models.CharField(max_length=3, choices=OPTIOS_FOR_APPOINTMENT_STATUS, verbose_name=_("وضعیت نوبت"))
    payment_status = models.BooleanField(default=False, verbose_name=_("وضعیت پرداخت"))

