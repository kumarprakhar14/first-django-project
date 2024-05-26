from django.db import models
from datetime import datetime

# Create your models here.
class Member(models.Model):
    fistname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.fistname} {self.lastname}"
