from django.db import models

class SignUp(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    re_password = models.CharField(max_length=50)