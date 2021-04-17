from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    officehours = models.CharField(max_length=20)

class Lab(models.Model):
    labid = models.CharField(max_length=20)
    labname = models.CharField(max_length=20)
    labschedule = models.CharField(max_length=20)
    labTA = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)


class Course(models.Model):
    courseid = models.CharField(max_length=20)
    coursename = models.CharField(max_length=20)
    courseschedule = models.CharField(max_length=20)
    coursecredits = models.CharField(max_length=20)
    # courseinstructor = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    courseTA = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    graders = models.CharField(max_length=20)
    labs = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)
