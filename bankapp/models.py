from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=9999)
    def __str__(self):
        return self.question