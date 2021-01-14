from django.db import models

# Create your models here.
class Food(models.Model):
    username = models.CharField(max_length=100)
    photo_url = models.TextField()

    