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

    # ASSIGN
    def test_setup(self):
        test_Sup = createAccount("testSup", "123", "email", "Supervisor", "123", "addr", "hours")
        test_Ins = createAccount("testIns", "123", "email", "Instructor", "123", "addr", "hours")
        test_TA = createAccount("testTA", "123", "email", "TA", "123", "addr", "hours")
        test_course1 = createCourse("1", "course1", "1")
        test_course2 = createCourse("2", "course2", "2")

    # ASSIGN INSTRUCTOR
    def test_assignInstructor_badParam(self):
        self.assertEqual(assignInstructor("", ""), "Please fill out all required fields")
        self.assertEqual(assignInstructor("", "testIns"), "Please fill out all required fields")
        self.assertEqual(assignInstructor("course1", ""), "Please fill out all required fields")

    def test_assignInstructor_goodParam(self):
        self.assertEqual(assignInstructor("course1", "testIns"), "")

    # ASSIGN TA
    def test_assignTAtoCourse_badParam(self):
        self.assertEqual(assignTAtoCourse("", "", "", ""), "Please fill out all required fields")
        self.assertEqual(assignTAtoCourse("1", "", "", ""), "Please fill out all required fields")
        self.assertEqual(assignTAtoCourse("", "testTA", "", ""), "Please fill out all required fields")
        self.assertEqual(assignTAtoCourse("", "", "1", ""), "Please fill out all required fields")
        self.assertEqual(assignTAtoCourse("", "", "", "True"), "Please fill out all required fields")

    def test_assignTAtoCourse_goodParam(self):
        self.assertEqual(assignTAtoCourse("1", "testTA", "1", "True"), "")

