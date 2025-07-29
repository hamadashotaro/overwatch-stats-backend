from django.db import models
from django.contrib.auth.models import User

class Stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # models.CASCADE on delete means that if the user is deleted, their stats will also be deleted.
    hero = models.CharField(max_length=30)
    map = models.CharField(max_length=30)
    game_mode = models.CharField(max_length=30)
    result = models.CharField(max_length=1, choices=[('W', 'Win'), ('L', 'Loss')])
    duo = models.CharField(max_length=30)

    def __str__(self):
        return f"Registered User: {self.user.username} - Hero: {self.hero} - Map: {self.map} - Game Mode: {self.game_mode} - Result: {self.result} - Duo: {self.duo}"