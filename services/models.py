from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Create your models here.


class Service(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    img = models.ImageField(_("service image"), upload_to='services/', height_field=50, width_field=50, max_length=1)
    title = models.TextField(_("service title"))
    price = models.IntegerField(_("service price"))
    duration = models.IntegerField(_("service duration"))
    description = models.TextField(_("service description"))
