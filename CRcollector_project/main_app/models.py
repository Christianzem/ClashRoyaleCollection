from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    rarity = models.CharField(max_length=100)
    cost = models.IntegerField()

    def __str__(self):
        return self.name