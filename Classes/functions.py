from project_app.models import *

def login(name, password):
    noSuchUser = False
    badPassword = False
    try:
        m = Users.objects.get(name)
        badPassword = (m.password != password)
    except:
        noSuchUser = True
    if noSuchUser or badPassword:
        return False
    else:
        return True

def create_course(id, name, schedule, instructor, TA, graderstatues, labs):
    try:
        i = Course.objects.get(id)
        return False

    except:
        return True


def createCourse(courseId="", courseName="", courseSchedule="", courseCredits=""):
    #precondition: courseid does not currently exist
    #postcondition: course is created with unique ID and name
    pass

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