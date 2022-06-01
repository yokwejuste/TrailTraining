from django.db import models

class First(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    image = 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
