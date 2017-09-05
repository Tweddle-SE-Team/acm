from django.db import models
from django.utils import timezone

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=9999)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    def __str__(self):
        return self.question

