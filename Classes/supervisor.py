from Classes.user import User
from Classes.course import Course
from Classes.lab import Lab

class Supervisor(User):

    def __init__(self, email):
        pass

    def delete_user(self):
        pass

    def view_data(self):
        pass

    def assigninstructor_tocourse(self, coursename, instructorname):
        pass

    def assignTA_tocourse(self, coursename, TAname):
        pass

    def assignTA_tolab(self, labname, TAname):
        pass

    def send_email(self, email):
        pass


