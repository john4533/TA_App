from project_app.models import *


def login(name, password):
    # precondition: user with provided username and password exists
    # postcondition: returns True if username and password match those in database, False if either entry is incorrect
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


def createAccount(username="", name="", password="", email="", role="", phone="", address="", officehours=""):
    # precondition: user with provided username does not currently exist with username, password, email, and role entered
    # postcondition: user account is created with a unique username, a password, an email, a role,
    # and a phone number, address and officehours if provided, returns a message if user already exists or required entries are not filled out
    if username != '' and name != '' and password != '' and email != '' and role != '':
        if len(list(User.objects.filter(username=username))) == 0:
            User.objects.create(username=username, name=name, password=password, email=email, role=role, phone=phone,
                                address=address, officehours=officehours)
            if role == "TA":
                user1 = User.objects.get(username=username)
                TA.objects.create(user=user1)
            string = ""
        else:
            string = "User with that username already exists"
    else:
        string = "Please fill out all required entries"
    return string


def createCourse(courseId="", name="", credits=""):
    # precondition: course with provided courseid does not currently exist with courseid, coursename, courseschedule, and coursecredits entered
    # postcondition: course is created with unique ID and name, message is returned if course with the id exists or required entries are blank
    if courseId != '' and name != '' and credits != '':
        if len(list(Course.objects.filter(courseid=courseId))) == 0:
            Course.objects.create(courseid=courseId, name=name, credits=credits)
            string = ""
        else:
            string = "Course with that ID already exists"
    else:
        string = "Please fill out all required entries"
    return string


def createSection(course="", sectionid="", types="", schedule=""):
    # precondition: course is given and exists, section with provided sectionid does not currently exist with sectionid, type, and sectionschedule entered
    # postcondition: section is created with unique sectionId and course, type, sectionschedule, message is returned if lab with the id exists or required entries are blank
    if course != '' and sectionid != '' and types != '' and schedule != '':

        if len(list(Section.objects.filter(sectionid=sectionid))) == 0:
            Section.objects.create(course=course, sectionid=sectionid, type=types, schedule=schedule)
            string = ""
        else:
            string = "Section with that ID already exists"
    else:
        string = "Please fill out all required entries"
    return string


def deleteAccount(username=""):
    # precondition: account with unique username exists
    # postcondition: account with unique username is removed from database and a message is returned if username is not entered,
    # if user with that username does not exist or if the user was successfully deleted
    if username == "":
        string = "Please enter a username"
    elif username not in list(i["username"] for i in User.objects.all().values("username")):
        string = "User with that username does not exist"
    else:
        User.objects.get(username=username).delete()
        string = "User with username " + username + " has been deleted"
    return string


def deleteCourse(courseid=""):
    # precondition: course with unique courseid exists
    # postcondition: course with unique courseid is removed from database and a message is returned if courseid is not entered,
    # if course with that courseid does not exist or if the course was successfully deleted
    if courseid == "":
        string = "Please enter a course ID"
    elif courseid not in list(i["courseid"] for i in Course.objects.all().values("courseid")):
        string = "Course with that ID does not exist"
    else:
        Course.objects.get(courseid=courseid).delete()
        string = "Course with ID " + courseid + " has been deleted"
    return string


def deleteSection(sectionid=""):
    # precondition: section with unique sectionid exists
    # postcondition: section with unique sectionid is removed from database and a message is returned if sectionid is not entered,
    # if section with that sectionid does not exist or if the section was successfully deleted
    if sectionid == "":
        string = "Please enter a section ID"
    elif sectionid not in list(i["sectionid"] for i in Section.objects.all().values("sectionid")):
        string = "Section with that ID does not exist"
    else:
        Section.objects.get(sectionid=sectionid).delete()
        string = "Section with ID " + sectionid + " has been deleted"
    return string


def assignInstructor(courseid="", instructor=""):
    # precondition: coursid of a current course and a unique instructor
    # postcondition: instuctor is assigned to the passed in course
    if instructor is None:
        string = "Please select an Instructor"
    else:
        string = ""
        courseid.Instructor = User.objects.get(username=instructor)
        courseid.save()

    return string


def assignTAtoCourse(courseid="", Username="", numLabs="", graderstatus=""):
    if not Username:
        message = "please select a user"
    elif not numLabs:
        message = "please enter number of labs"
    else:
        message = ""
        ta = TA.objects.get(user__username=(User.objects.get(username=Username)).username)
        ta.course = courseid
        ta.numlabs = numLabs
        ta.save()
        if graderstatus:
            ta.graderstatus = graderstatus
            ta.save()
    return message


def assignTAtoSection(sectionid="", username=""):
    if username is None:
        message = "please select a user"
        print(username)
    else:
        message = ""
        s = Section.objects.get(sectionid=sectionid)
        t = TA.objects.get(user__username=username)
        s.TA_assigned = t
        s.save()
    return message


def getCourses():
    # precondition: None
    # postcondition: returns a dictionary with course keys and values are lists of section
    courses = list(Course.objects.all())
    dictionary = {}
    for c in courses:
        dictionary[c] = list(Section.objects.filter(course__courseid=c.courseid))
    return dictionary


def getTAsInCourse(sectionid):
    # precndition: courseid
    # postcondition: returns a dictionary of TAs in a particular course
    s = Section.objects.get(sectionid=sectionid)
    return list(TA.objects.filter(course__courseid=s.course.courseid))

def unAssignTA(name):
    user1=User.objects.get(username=name)
    ta=TA.objects.get(user=user1)
    section = Section.objects.get(TA_assigned=ta)
    section.TA_assigned=None
    section.save()
    ta.course=None
    ta.save()
    return "TA is Unassigned from this course"

def unAssignTASection(sectionid):
    section=Section.objects.get(sectionid=sectionid)
    section.TA_assigned=None
    section.save()
    return "TA has been unassigned from this section"

def unAssignInstructor(courseid):
    course=Course.objects.get(courseid=courseid)
    course.Instructor=None
    course.save()
    return "Instructor has been unassigned from this course"