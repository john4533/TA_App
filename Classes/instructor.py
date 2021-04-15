from Classes.user import User
from Classes.lab import Lab

class Instructor(User):

    def __init__(self, name, qualifications, officehours, email):
        pass

    def edit_instructorqualifications(self, qualifications):
        pass

    def edit_instructorofficehours(self, officehours):
        pass

    def assignTA_tolab(self, labname, TAname):
        pass

    def send_email(self, email):
        pass