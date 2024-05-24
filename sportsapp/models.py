from django.db import models

# Create your models here.

class Athlete(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    sport = models.CharField(max_length=100)
    achievements = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"