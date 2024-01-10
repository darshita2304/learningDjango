from django.db import models

# Create your models here.
class Login(models.Model):
  login = models.CharField(max_length=255)
  pwd = models.CharField(max_length=255)