from django.test import TestCase
import os
from Classes.functions import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()

from project_app.models import Course, Lab


class MyTestCase(TestCase):

#   CREATE COURSE TESTS
    def test_courseIdexists(self):
        Course.objects.create(courseid="337", coursename="Systems Programming", courseschedule="TR @ 1:00 - 1:50", coursecredits="3")
        self.assertEqual(createCourse("337", "Software Engineering", "TR @ 10:00 - 10:50", "3"), "Course with that ID already exists")

    def test_courseCreated(self):
        createCourse("361", "Software Engineering", "TR @ 10:00 - 10:50", "3")
        b = Course.objects.get(courseid="361")
        self.assertEqual("Software Engineering", b.coursename)
        self.assertEqual("TR @ 10:00 - 10:50", b.courseschedule)
        self.assertEqual("3", b.coursecredits)

    def test_nocourseid(self):
        self.assertEqual(createCourse("", "Software Engineering", "TR @ 10:00 - 10:50", "3"), "Please fill out all required entries")

    def test_nocoursename(self):
        self.assertEqual(createCourse("361", "", "TR @ 10:00 - 10:50", "3"), "Please fill out all required entries")

    def test_nocourseschedule(self):
        self.assertEqual(createCourse("361", "Software Engineering", "", "3"), "Please fill out all required entries")

    def test_nocoursecredits(self):
        self.assertEqual(createCourse("361", "Software Engineering", "TR @ 10:00 - 10:50", ""), "Please fill out all required entries")



#   DELETE COURSE TESTS
    def test_deletenocourseidentered(self):
        self.assertEqual(deleteCourse(""), "Please enter a course ID")

    def test_deletenocourseexists(self):
        self.assertEqual(deleteCourse("361"), "Course with that ID does not exist")

    def test_deletecourse(self):
        course1 = Course.objects.create(courseid="337", coursename="Systems Programming", courseschedule="TR @ 1:00 - 1:50", coursecredits="3")
        self.assertEqual(course1.courseid, "337")
        self.assertEqual(deleteCourse("337"), "Course with ID 337 has been deleted")

#   GET COURSES TESTS
    def test_getCourses_noCourses(self):
        self.assertEqual(getCourses(), {})

    def test_getCourses_noLabs(self):
        course1 = Course.objects.create(courseid="337", coursename="Systems Programming", courseschedule="TR @ 1:00 - 1:50", coursecredits="3")
        self.assertEqual(getCourses(), {course1: []})

    def test_getCourses_success(self):
        course1 = Course.objects.create(courseid="337", coursename="Systems Programming", courseschedule="TR @ 1:00 - 1:50", coursecredits="3")
        lab1 = Lab.objects.create(course=course1, labid="901", labname="Lab 1", labschedule="T @ 11:00 - 12:50")
        self.assertEqual(getCourses(), {course1: [lab1]})


    # def test_courseIdupdated(self):
    #     createCourse("361", "Software Engineering", "TR - 10:00", "3")
    #     setCourseId("362", "361")
    #     b = Course.objects.get(courseid="362")
    #     self.assertEqual("Software Engineering", b.coursename)
    #     self.assertEqual("TR - 10:00", b.courseschedule)
    #     self.assertEqual("3", b.coursecredits)
    #
    # def test_courseNameupdated(self):
    #     createCourse("361", "Software Engineering", "TR - 10:00", "3")
    #     setCourseName("Not Software Engineering", "361")
    #     b = Course.objects.get(courseid="361")
    #     self.assertEqual("Not Software Engineering", b.coursename)
    #
    # def test_courseScheduleupdated(self):
    #     createCourse("361", "Software Engineering", "TR - 10:00", "3")
    #     setCourseSchedule("MW - 12:00", "361")
    #     b = Course.objects.get(courseid="361")
    #     self.assertEqual("MW - 12:00", b.courseschedule)
    #
    # def test_courseCreditsupdated(self):
    #     createCourse("361", "Software Engineering", "TR - 10:00", "3")
    #     setCourseCredits("4", "361")
    #     b = Course.objects.get(courseid="361")
    #     self.assertEqual("4", b.coursecredits)
