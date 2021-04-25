from project_app.models import *

def login(name, password):
    noSuchUser = False
    badPassword = False
    try:
        m = User.objects.get(username=name)
        badPassword = (m.password != password)
    except:
        noSuchUser = True
    if noSuchUser or badPassword:
        return False
    else:
        return True

def createAccount(username="", password="", email="", role=""):
    # precondition: user with provided email does not currently exist
    # postcondition: user account is created with a unique email and role
    if username != '' and password != '' and email != '' and role != '':
        if len(list(User.objects.filter(email=email))) == 0:
            User.objects.create(username=username, password=password, email=email, role=role)
        else:
            return "User with that email already exists"
    else:
        return "Please fill out all required entries"

def createCourse(courseId="", courseName="", courseSchedule="", courseCredits=""):
    # precondition: courseid does not currently exist
    # postcondition: course is created with unique ID and name, message is returned if course with the id exists
    if courseId != '' and courseName != '' and courseSchedule != '' and courseCredits != '':
        if len(list(Course.objects.filter(courseid=courseId))) == 0:
            Course.objects.create(courseid=courseId, coursename=courseName, courseschedule=courseSchedule, coursecredits=courseCredits)
        else:
            return "Course with that ID already exists"
    else:
        return "Please fill out all required entries"

def setCourseId(courseId, courseIdOriginal):
    #precondition: course with the old ID exists, new ID does not exist
    #postcondition: course ID is updated
    pass

def setCourseName(courseName, courseId):
    #precondition: course with the ID exists
    #postcondition: course name is updated
    pass

def setCourseSchedule(courseSchedule, courseId):
    # precondition: course with the ID exists
    # postcondition: course schedule is updated
    pass

def setCourseCredits(courseCredits, courseId):
    #precondition: course with the ID exists
    #postcondition: course credits are updated
    pass


# MAYBE IMPLEMENT THESE LATER
# def setCourseInstructor(courseInstructor, courseId):
#     # precondition: course with the ID exists
#     # postcondition: course instructor is updated
#     pass
#
# def setCourseTA(courseTA, courseId):
#     # precondition: course with the ID exists
#     # postcondition: course TA is updated
#     pass


def createLab(labId, labName):
    # Precondition: correct two inputs, and labId does not already belong to a lab
    # Postcondition: lab is created with the given labId and labName
    pass


def setLabId(labIdNew, labIdOriginal):
    # Precondition: correct two inputs, labIdOriginal needs to exist already, and labIdNew needs to not exist already
    # Postcondition: new labId is assigned to the lab
    pass


def setLabName(labName, labId):
    # Precondition: correct two inputs, and labId needs to exist already
    # Postcondition: labName is assigned to the lab
    pass


def setLabSchedule(schedule, labId):
    # Precondition: correct two inputs,
    # Postcondition: labSchedule is assigned to the lab
    pass


def setLabTA(ta, labId):
    # Precondition: correct two inputs, and labId needs to exist already
    # Postcondition: ta is assigned to the lab
    pass

def deleteaccount(username):
    pass

def deleteCourse(courseid=""):
    if courseid == "":
        return "Please enter a course ID"
    elif courseid not in list(i["courseid"] for i in Course.objects.all().values("courseid")):
        return "Course with that ID does not exist"
    else:
        Course.objects.get(courseid=courseid).delete()
        return "Course with ID " + courseid + " has been deleted"


