from django.db import models

# Create your models here.
class PersonSalary(models.Model):
    age = models.PositiveBigIntegerField()
    salary = models.FloatField()
    education = models.CharField(max_length=128)