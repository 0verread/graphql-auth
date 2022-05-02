from django.db import models
from django.utils import timezone

class Users(models.Model):
  id = models.CharField(max_length=12, primary_key=True)
  full_name = models.CharField(max_length=256, blank=True)
  username = models.CharField(max_length=256, unique=True, blank=False)
  email = models.EmailField(unique=True)
  password = models.TextField(blank=False)
  date_joined = models.DateTimeField(default=timezone.now, editable=False)
  class Meta:
    db_table = 'users'
    managed = False

class Salts(models.Model):
  user_id = models.CharField(max_length=12)
  pass_salt = models.CharField(max_length=10)

  class Meta:
    db_table = 'salts'
    managed = False