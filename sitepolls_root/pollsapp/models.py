from django.db import models
from datetime import datetime


# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.question


class Choice(models.Model):
    choice = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)
    question_rel = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice