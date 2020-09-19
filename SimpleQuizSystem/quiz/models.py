from django.db import models

# class to refer tables in DB
class Exam(models.Model):
    Question = models.CharField(max_length = 100)
    Option1 = models.CharField(max_length = 100)
    Option2 = models.CharField(max_length = 100)
    Option3 = models.CharField(max_length = 100)
    Option4 = models.CharField(max_length = 100)
    Corrans = models.CharField(max_length = 100)
