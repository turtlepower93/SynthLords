from django.db import models

# Create your models here.

class Synth(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    s_type = models.CharField(max_length=40)
    rating = models.IntegerField()

def __str__(self):
    return self.name