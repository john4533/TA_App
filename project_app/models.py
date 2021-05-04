from django.db import models


# Create your models here.
class Roles(models.TextChoices):
    sup = "Supervisor"
    ta = "TA"
    ins = "Instructor"



class Types(models.TextChoices):
    lec = "Lecture"
    lab = "Lab"
    disc = "Discussion"

class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=10, choices=Roles.choices)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    officehours = models.CharField(max_length=20, blank=True)
    skills=models.CharField(max_length=200,blank=True)

class Course(models.Model):
    courseid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    credits = models.CharField(max_length=2)
    Instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class TA(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    graderstatus = models.BooleanField(default=False)
    numlabs = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    sectionid = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=Types.choices)
    schedule = models.CharField(max_length=20, blank=True)
    TA_assigned = models.ForeignKey(TA, on_delete=models.SET_NULL, blank=True, null=True)

