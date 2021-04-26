from django.db import models


# Create your models here.
class Roles(models.TextChoices):
    sup = "Supervisor"
    ta = "TA"
    ins = "Instructor"

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=10, choices=Roles.choices)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    officehours = models.CharField(max_length=20, blank=True)

class Course(models.Model):
    courseid = models.CharField(max_length=20)
    coursename = models.CharField(max_length=50)
    courseschedule = models.CharField(max_length=20, blank=True)
    coursecredits = models.CharField(max_length=2)

class Lab(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    labid = models.CharField(max_length=20)
    labname = models.CharField(max_length=50)
    labschedule = models.CharField(max_length=20, blank=True)

