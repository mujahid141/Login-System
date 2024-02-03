# myapp/models.py
from django.db import models

class CustomUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    major = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # Store password hashes for security

    def __str__(self):
        return self.username
