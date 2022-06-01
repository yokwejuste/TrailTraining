from django.db import models

class Subjects(models.Model):
    name = models.CharField(max_length=50, null=False)
    code = models.CharField(max_length=10, primary_key=True, null=False)
    lecturer = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Subjects"

    def __str__(self, name):
        return name
