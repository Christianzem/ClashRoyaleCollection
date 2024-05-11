from django.db import models
from django.urls import reverse


STATUS = (
    ('1', 'LEVEL 1'),
    ('2', 'LEVEL 2'),
    ('3', 'LEVEL 3'),
    ('4', 'LEVEL 4'),
    ('5', 'LEVEL 5'),
    ('6', 'LEVEL 6'),
    ('7', 'LEVEL 7'),
    ('8', 'LEVEL 8'),
    ('9', 'LEVEL 9'),
    ('10', 'LEVEL 10'),
    ('11', 'LEVEL 11'),
    ('12', 'LEVEL 12'),
    ('13', 'LEVEL 13'),
    ('14', 'LEVEL 14'),
)

class Player(models.Model):
    player_name = models.CharField(max_length=100)

    def __str__(self):
        return self.player_name
    
    def get_absolute_url(self):
        return reverse('players_detail', kwargs={'pk': self.id})
    
# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    rarity = models.CharField(max_length=100)
    cost = models.IntegerField()
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'card_id': self.id})
    
class Status(models.Model):
    date = models.DateField('Upgraded on')
    status = models.CharField(max_length=14, choices=STATUS, default=STATUS[0][0])
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_status_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
    