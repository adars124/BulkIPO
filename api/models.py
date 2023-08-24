from django.db import models

# Create your models here.
class Info(models.Model):
    clientId = models.PositiveIntegerField(default=0)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    crn = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)

    def __str__(self):
        return str(self.clientId)