from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    rollno = models.IntegerField()
    number =models.IntegerField()
    course = models.CharField(max_length=255)

    def __str__(self):
        return self.name
