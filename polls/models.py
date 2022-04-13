import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    random = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    sum = models.IntegerField(default=0)
    slug = models.SlugField(max_length=25, default=6)
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    max = models.IntegerField(default=-1)
    min = models.IntegerField(default=10000)
    sum = models.IntegerField(default=0)
    percent = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text



		
    
    