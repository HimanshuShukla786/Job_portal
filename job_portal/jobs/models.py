from turtle import position
from django.db import models
from django.contrib.auth.models import User


class job(models.Model):
    """
    - Position name
    - Text Description
    - Age Criteria
    - Salary
    - No. of openings
    """
    position_name =models.CharField(max_length=100)
    text_description = models.TextField()
    min_age =models.IntegerField()
    max_age =models.IntegerField()
    salary =models.IntegerField()
    no_openongs =models.IntegerField()
    create= models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.position_name