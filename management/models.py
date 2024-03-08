from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=20)
    capacity = models.IntegerField()

    def __str__(self):
        return self.room_number

