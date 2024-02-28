from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    field_of_interest = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.user.username
        
