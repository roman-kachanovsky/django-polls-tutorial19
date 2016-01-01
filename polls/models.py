import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # Helpful representation of this object
    def __str__(self): # __unicode__ if you use Python 2.x
        return self.question_text
    # Custom method
    def was_published_recently(self):
        # Before fixing a bug
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # After
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # Helpful representation of this object
    def __str__(self): # __unicode__ if you use Python 2.x
        return self.choice_text
