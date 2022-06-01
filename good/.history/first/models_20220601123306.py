from django.db import models

class First(models.Model):
    name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
