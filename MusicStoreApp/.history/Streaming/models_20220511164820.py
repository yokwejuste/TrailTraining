from django.db import models

class Subjects(models.Model):
    name = models.CharField(max_length=50, null=False)
    code = models.CharField(max_length=10)
    lecturer = models.CharField(max_length=100)
    added_on = models.AutoField(null=False)
