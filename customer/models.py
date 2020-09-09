from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    
    name = models.CharField(blank=False, max_length=255)
    email = models.CharField(blank=False, max_length=255)
    company = models.CharField(blank=True, null=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name