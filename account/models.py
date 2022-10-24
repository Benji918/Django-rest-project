from django.core.validators import EmailValidator
from django.db import models


# Create your models here.
class Registration(models.Model):
    fname = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(validators=[EmailValidator], null=False, blank=False)
    pwd = models.CharField(max_length=20, null=False, blank=False)


class Login(models.Model):
    email = models.EmailField(validators=[EmailValidator], null=False, blank=False)
    pwd = models.CharField(max_length=20, null=False, blank=False)


