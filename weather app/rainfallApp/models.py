from django.db import models

# Create your models here.

class Rainfall(models.Model):
    day = models.CharField(max_length=50)
    rainfall = models.IntegerField()

    def __str__(self):
        return f" it rained {self.rainfall} millimetres on {self.day}"

