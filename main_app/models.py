from django.db import models
from django.urls import reverse

# Create your models here.

CATEGORIES = (
    ('B', 'Bass'),
    ('L', 'Lead'),
    ('P', 'Pad'),
    {'K', 'DrumKit'}
)

class Synth(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    s_type = models.CharField(max_length=40)
    rating = models.IntegerField()

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('details', kwargs={'synth_id': self.id})

class Patch(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
        )
    author = models.CharField(max_length=50)

    synth = models.ForeignKey(Synth, on_delete=models.CASCADE)

    def __str__(self):
        return f" PATCH->CANNONTYPE: {self.get_category_display()}"