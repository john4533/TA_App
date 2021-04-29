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
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=10, choices=Roles.choices)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    officehours = models.CharField(max_length=20, blank=True)


class Course(models.Model):
    courseid = models.CharField(max_length=20)
    coursename = models.CharField(max_length=50)
    coursecredits = models.CharField(max_length=2)
    user_assigned= models.ForeignKey(User,on_delete=models.CASCADE)

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    sectionid = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=Types.choices)
    schedule = models.CharField(max_length=20, blank=True)
    #TA = models.ForeignKey(TA, on_delete=models.CASCADE)

# class TA(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     graderstatus = models.BooleanField(False)
#     numlabs = models.CharField(max_length=1)