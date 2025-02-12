from django.db import models
from account.models import User
from django.utils.translation import gettext_lazy as _
# choices
OPTIOS_FOR_APPOINTMENT_STATUS = [
    ('P' , 'Pending'),
    ('C' , 'Confirmed'),
    ('R' , 'Rejected')
]
# models
class BookingSalon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    service = 1
    date = models.DateTimeField(auto_now_add=True)
    appointment_date = 1
    status = models.CharField(max_length=3, choices=OPTIOS_FOR_APPOINTMENT_STATUS, verbose_name=_("status"))
    payment_status = models.BooleanField(default=False, verbose_name=_("payment_status"))

    def __str__(self):
        return f"{self.user} | service:{self.service} | date:{self.appointment_date}"

