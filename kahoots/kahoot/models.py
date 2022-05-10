import datetime

from django.db import models
from django import utils
from random import randint

def generate_game_code():
    return randint(111111, 999999)


class Participant(models.Model):
    join_time = models.DateTimeField('date joined', default=utils.timezone.now)
    nickname = models.CharField(max_length=30)
    score = models.IntegerField(default=0)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)


class Game(models.Model):
    STATUSES = [
        (0, 'Initialized'),
        (1, 'Started'),
        (2, 'ended')
    ]

    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    start_time = models.DateTimeField('date published', default=utils.timezone.now)
    code = models.IntegerField(default=generate_game_code)
    status = models.IntegerField(choices=STATUSES, default=0)
    current_question = models.IntegerField(default=1)


class Quiz(models.Model):
    name = models.CharField(max_length=200, default='New quiz')
    pub_date = models.DateTimeField('date published', default=utils.timezone.now)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=utils.timezone.now)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

