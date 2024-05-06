from django.db import models

# Create your models here.

course_choices = (
    ('IT', 'InformationTechnology'),
    ('CE', 'ComputerEngineering'),
)

class Student(models.Model):
    name = models.CharField(max_length=255)
    rollno = models.IntegerField()
    course = models.CharField(choices=course_choices, max_length=2)

    def __str__(self):
        return self.name