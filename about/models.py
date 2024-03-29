from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)