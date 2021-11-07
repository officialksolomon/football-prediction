from django.db import models
from django.contrib.auth.models import User
from django.utils import tree
# Create your models here.
from datetime import datetime


class Match(models.Model):
    pub_date = models.DateTimeField("Published on")
    game_date = models.DateTimeField("Game date")
    team_one = models.CharField(max_length=100, blank=True)
    team_two = models.CharField(max_length=100, blank=True)
    result = models.CharField(max_length=50, blank=True)
    completed = models.BooleanField()

    def __str__(self):
        return f"{self.team_one} vs {self.team_two}"


class Prediction(models.Model):
    pub_date = models.DateTimeField("Date & Time", auto_now=True)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    prediction = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return f"{self.prediction}"
