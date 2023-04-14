from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.subject
class Diagnosis(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
class GPTResponse(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content