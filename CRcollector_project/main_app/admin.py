from django.contrib import admin
from .models import Card, Status, Player

# Register your models here.
admin.site.register(Card)
admin.site.register(Status)
admin.site.register(Player)