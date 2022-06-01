from django.db import models

class First(models.Model):
    name = models.CharField(max_length=255, null=T)
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
