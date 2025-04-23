from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    '''従業員のモデル'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True) #254文字
    department = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username if self.user else 'No User'})"
