
class User():

    def __init__(self, name, password):
        pass

    def create_user(self, name, password):
        pass

    def login(self, name, password):
        pass

class Course():


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


class Lab(Course):


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

class Supervisor(User):


    def __init__(self, name, email):
        pass

class AssignInstructor():

    def assigninstructor_tocourse(self, coursename, instructorname):
        pass

class AssignTA():

    def assignTA_tocourse(self, coursename, TAname):
        pass

    def assignTA_tolab(self, labname, TAname):
        pass

class Instructor(User):


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

class Email():


    def send_email(self, email):
        pass

class TA(User):


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

class Student(User):


    def __init__(self, name, email):
        pass

    def edit_studentname(self, name):
        pass

