from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import ugettext as _
from django.conf import settings
from django.utils import timezone
from account.managers import CustomUserManager

class MyUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("First name"), max_length=50)
    last_name = models.CharField(_("Last name"), max_length=50)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_("Username"), max_length=100)
    bio = models.TextField(_("User bio"), blank = True, null = True)
    profile_img = models.ImageField(_("Profile Image"), upload_to='profile-pictures/',blank = True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    