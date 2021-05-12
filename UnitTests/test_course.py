from django.test import TestCase
import os
from Classes.functions import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()


class CourseTestCase(TestCase):

#   CREATE COURSE TESTS
    def test_courseIdexists(self):
        Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        self.assertEqual(createCourse("337", "Software Engineering", "3"), "Course with that ID already exists")

    def test_courseCreated(self):
        createCourse("361", "Software Engineering", "3")
        b = Course.objects.get(courseid="361")
        self.assertEqual("Software Engineering", b.name)
        self.assertEqual("3", b.credits)

    def test_nocourseid(self):
        self.assertEqual(createCourse("", "Software Engineering", "3"), "Please fill out all required entries")

    def test_nocoursename(self):
        self.assertEqual(createCourse("361", "", "3"), "Please fill out all required entries")


    def test_nocoursecredits(self):
        self.assertEqual(createCourse("361", "Software Engineering", ""), "Please fill out all required entries")

#   DELETE COURSE TESTS
    def test_deletenocourseidentered(self):
        self.assertEqual(deleteCourse(""), "Please enter a course ID")

    def test_deletenocourseexists(self):
        self.assertEqual(deleteCourse("361"), "Course with that ID does not exist")

    def test_deletecourse(self):
        course1 = Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        self.assertEqual(course1.courseid, "337")
        self.assertEqual(deleteCourse("337"), "Course with ID 337 has been deleted")

#   GET COURSES TESTS
    def test_getCourses_noCourses(self):
        self.assertEqual(getCourses(), {})

    def test_getCourses_noLabs(self):
        course1 = Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        self.assertEqual(getCourses(), {course1: []})

    def test_getCourses_success(self):
        course1 = Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        section= Section.objects.create(course=course1, sectionid="901", type="Lab 1",schedule="T @ 11:00 - 12:50")
        self.assertEqual(getCourses(), {course1: [section]})

    # ASSIGN INSTRUCTOR
    def test_assignInstructor_badParam(self):
        test_Ins = User.objects.create(username="testInsUser", name="testInsName", password="123",
                                       email="testIns@uwm.edu", role="Instructor", phone="123-456-7890",
                                       address="testInsAddress", officenumber="E252", officehoursStart="10:00",
                                       officehoursEnd="10:50", officehoursDays=[], skills="")
        test_course1 = Course.objects.create(courseid="361", name="Test Course 1", credits="3")

        self.assertEqual(assignInstructor(None, None), "Please select a course")
        self.assertEqual(assignInstructor("", ""), "Please select a course")
        self.assertEqual(assignInstructor(None, "testInsUser"), "Please select a course")
        self.assertEqual(assignInstructor("", "testInsUser"), "Please select a course")
        self.assertEqual(assignInstructor(test_course1, None), "Please select an instructor")
        self.assertEqual(assignInstructor(test_course1, ""), "Please select an instructor")

    def test_assignInstructor_goodParam(self):
        test_Ins = User.objects.create(username="testInsUser", name="testInsName", password="123",
                                       email="testIns@uwm.edu", role="Instructor", phone="123-456-7890",
                                       address="testInsAddress", officenumber="E252", officehoursStart="10:00",
                                       officehoursEnd="10:50", officehoursDays=[], skills="")
        test_course1 = Course.objects.create(courseid="361", name="Test Course 1", credits="3")

        self.assertEqual(assignInstructor(test_course1, "testInsUser"), "")

    # ASSIGN TA TO COURSE
    def test_assignTAtoCourse_badParam(self):
        test_TA_User = User.objects.create(username="testTAUser", name="testTAName", password="123",
                                           email="testTA@uwm.edu", role="TA", phone="123-456-7890",
                                           address="testTAAddress", officenumber="E253", officehoursStart="1:00",
                                           officehoursEnd="2:00", officehoursDays=[], skills="")
        test_course1 = Course.objects.create(courseid="361", name="Test Course 1", credits="3")
        test_TA_TA = TA.objects.create(user=test_TA_User, graderstatus=False, numlabs=0, course=test_course1,
                                       assignedlabs=0)
        self.assertEqual(assignTAtoCourse("", "", "", ""), "Please select a course")
        self.assertEqual(assignTAtoCourse(None, None, None, None), "Please select a course")

        self.assertEqual(assignTAtoCourse("", "testTAUser", 1, True), "Please select a course")
        self.assertEqual(assignTAtoCourse(None, "testTAUser", 1, True), "Please select a course")

        self.assertEqual(assignTAtoCourse(test_course1, "", 1, True), "Please select a TA")
        self.assertEqual(assignTAtoCourse(test_course1, None, 1, True), "Please select a TA")

        self.assertEqual(assignTAtoCourse(test_course1, "testTAUser", "", True), "Please enter the number of labs")
        self.assertEqual(assignTAtoCourse(test_course1, "testTAUser", None, True), "Please enter the number of labs")
        self.assertEqual(assignTAtoCourse(test_course1, "testTAUser", -1, True), "Please enter the number of labs")

    def test_assignTAtoCourse_goodParam(self):
        test_TA_User = User.objects.create(username="testTAUser", name="testTAName", password="123",
                                           email="testTA@uwm.edu", role="TA", phone="123-456-7890",
                                           address="testTAAddress", officenumber="E253", officehoursStart="1:00",
                                           officehoursEnd="2:00", officehoursDays=[], skills="")
        test_course1 = Course.objects.create(courseid="361", name="Test Course 1", credits="3")
        test_TA_TA = TA.objects.create(user=test_TA_User, graderstatus=False, numlabs=0, course=test_course1,
                                       assignedlabs=0)
        self.assertEqual(assignTAtoCourse(test_course1, "testTAUser", 1, True), "")

    # ASSIGN TA TO SECTION
    def test_assignTAtoSection_badParam(self):
        test_TA_User = User.objects.create(username="testTAUser", name="testTAName", password="123",
                                           email="testTA@uwm.edu", role="TA", phone="123-456-7890",
                                           address="testTAAddress", officenumber="E253", officehoursStart="01:00",
                                           officehoursEnd="02:00", officehoursDays=[], skills="")
        test_course1 = Course.objects.create(courseid="361", name="Test Course 1", credits="3")
        test_TA_TA = TA.objects.create(user=test_TA_User, graderstatus=False, numlabs=0, course=test_course1,
                                       assignedlabs=0)
        test_section1 = Section.objects.create(course=test_course1, sectionid="201", type="Lecture",
                                               scheduleStart="11:00", scheduleEnd="12:45", scheduleDays="T",
                                               TA_assigned=None)

        self.assertEqual(assignTAtoSection("", ""), "Please select a section")
        self.assertEqual(assignTAtoSection(None, None), "Please select a section")
        self.assertEqual(assignTAtoSection("", "testTAUser"), "Please select a section")
        self.assertEqual(assignTAtoSection(None, "testTAUser"), "Please select a section")
        self.assertEqual(assignTAtoSection("201", ""), "Please select a TA")
        self.assertEqual(assignTAtoSection("201", None), "Please select a TA")

    def test_assignTAtoSection_goodParam(self):
        test_TA_User = User.objects.create(username="testTAUser", name="testTAName", password="123",
                                           email="testTA@uwm.edu", role="TA", phone="123-456-7890",
                                           address="testTAAddress", officenumber="E253", officehoursStart="01:00",
                                           officehoursEnd="02:00", officehoursDays=[], skills="")
        test_course1 = Course.objects.create(courseid="361", name="Test Course 1", credits="3")
        test_TA_TA = TA.objects.create(user=test_TA_User, graderstatus=False, numlabs=0, course=test_course1,
                                       assignedlabs=0)
        test_section1 = Section.objects.create(course=test_course1, sectionid="201", type="Lecture",
                                               scheduleStart="11:00", scheduleEnd="12:45", scheduleDays="T",
                                               TA_assigned=None)

        self.assertEqual(assignTAtoSection("201", "testTAUser"), "")

