from django.db import models

class Employee(models.Model):
    '''従業員のモデル'''
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True) #254文字
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
