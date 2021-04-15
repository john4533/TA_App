from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __init__(self, name, password):
        pass

    def create_user(self, name, password):
        pass

    def login(self, name, password):
        pass

class Course(models.Model):


    def __init__(self, name, description, schedule):
        pass

    def edit_coursename(self, name):
        pass

    def edit_coursedescription(self, name):
        pass

    def edit_courseschedule(self, schedule):
        pass

    def delete_course(self, name, description, schedule):
        pass


class Lab(models.Model, Course):


    def __init__(self, name, description, schedule):
        pass

    def edit_labname(self, name):
        pass

    def edit_labdescription(self, description):
        pass

    def edit_labschedule(self, schedule):
        pass

    def delete_lab(self, name, description, schedule):
        pass

class Supervisor(models.Model, User):


    def __init__(self, name, email):
        pass

class AssignInstructor(models.Model):

    def assigninstructor_tocourse(self, coursename, instructorname):
        pass

class AssignTA(models.Model):

    def assignTA_tocourse(self, coursename, TAname):
        pass

    def assignTA_tolab(self, labname, TAname):
        pass

class Instructor(models.Model, User):


    def __init__(self, name, qualifications, officehours, email):
        pass

    def edit_instructorname(self, name):
        pass

    def edit_instructorqualifications(self, qualifications):
        pass

    def edit_instructorofficehours(self, officehours):
        pass

    def delete_instructor(self, name, qualifications, officehours, email):
        pass

class Email(models.Model):


    def send_email(self, email):
        pass

class TA(models.Model, User):


    def __init__(self, name, qualifications, officehours, email):
        pass

    def edit_TAname(self, name):
        pass

    def edit_TAqualifications(self, qualifications):
        pass

    def edit_TAofficehours(self, officehours):
        pass

    def delete_TA(self, name, qualifications, officehours, email):
        pass

class Student(models.Model, User):


    def __init__(self, name, email):
        pass

    def edit_studentname(self, name):
        pass


