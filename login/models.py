from django.db import models

# Create your models here.
class Login(models.Model):
  login = models.CharField(max_length=255)
  pwd = models.CharField(max_length=255)
  firstname = models.CharField(max_length=255, default='')
  lastname = models.CharField(max_length=255, default='')
  phone = models.IntegerField(default=0)
  joined_date = models.DateField(default='',null=True, blank=True)