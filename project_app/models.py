from django.db import models


# Create your models here.
class Roles(models.TextChoices):
    supervisor = "supervisor"
    TA = "TA"
    instructor = "instructor"

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=10, choices=Roles.choices)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)

    # officehours may need to be a sort of datetime object
    officehours = models.CharField(max_length=20, blank=True)

class Lab(models.Model):
    labid = models.CharField(max_length=20)
    labname = models.CharField(max_length=50)

    # labschedule may need to be a sort of datetime object
    labschedule = models.CharField(max_length=20, blank=True)
    # labTA = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Course(models.Model):
    courseid = models.CharField(max_length=20)
    coursename = models.CharField(max_length=50)

    # courseschedule may need to be a sort of datetime object
    courseschedule = models.CharField(max_length=20, blank=True)
    coursecredits = models.CharField(max_length=2)

    # courseinstructor = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    # courseTA may be a list including foreign key to the TA user, a graderstatus boolean, and # number of labs they are in
    # courseTA = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # graderstatus = models.BooleanField(default=False)
    # labs = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True)
