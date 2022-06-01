from django.db import models

class First(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
