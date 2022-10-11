from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models
from django.urls import reverse
from .managers import UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    car_licence = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    class Role(models.TextChoices):
        AGENT = 'a', _('Agent')
        USER = 'u', _('User')
        SUPERVISOR = 's', _('Supervisor')

    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.USER,
    )

    class StatusTypes(models.TextChoices):
        AVAILABLE = 'av', _('Available')
        UNAVAILABLE = 'un', _('Unavailable')
        OCCUPIED = 'oc', _('Occupied')

    status = models.CharField(
        max_length=2,
        choices=StatusTypes.choices,
        default=StatusTypes.AVAILABLE,
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return reverse('Fuel:login')

    def __str__(self):
        return str(self.username) + " - " + str(self.role)

    def __eq__(self, __o: object) -> bool:
        if __o:
            return self.username == __o.username
        return False


class FuelRequest(models.Model):
    class Status(models.TextChoices):
        LOOKING_FOR_AGENT = 'looking_for_agent'
        IN_PROGRESS = 'in_progress'
        SUCCESSFUL = 'successful'

    created_at = models.DateTimeField(auto_now_add=True)
    supervisor = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='supervisor_nazer')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, unique=False, related_name='requesting_user')
    agent = models.ForeignKey(User, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='driver_agent')
    status = models.CharField(
        max_length=25, choices=Status.choices, default=Status.LOOKING_FOR_AGENT)
    address = models.CharField(max_length=200, default="")
    amount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username) + ' - ' + str(self.created_at)
