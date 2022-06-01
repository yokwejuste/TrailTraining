from django.db import models

class Subjects(models.Model):
    name = models.CharField(max_length=50, null=False)
    code = models.CharField(max_length=10, primary_key=True, null=False)
    lecturer = models.CharField(max_length=100, null=)
    added_on = models.AutoField(null=False)
