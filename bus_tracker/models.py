from django.db import models

class BusStop(models.Model):
    name = models.CharField(max_length=100)
    passengers_waiting = models.BooleanField(default=False)  # True if passengers are waiting

    def __str__(self):
        return self.name
