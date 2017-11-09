from django.db import models

from django.contrib.auth.models import User

class Project(models.Model):
    slug = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
