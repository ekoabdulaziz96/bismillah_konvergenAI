from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

from .models_role import Role as RoleModel


class User(AbstractUser):
  pass
  # role = models.ForeignKey(RoleModel, on_delete=models.CASCADE, null=True)


