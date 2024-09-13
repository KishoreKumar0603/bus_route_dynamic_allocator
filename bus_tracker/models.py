from django.db import models

class BusStop(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=0.0)  
    longitude = models.FloatField(default=0.0) 

    def __str__(self):
        return self.name
