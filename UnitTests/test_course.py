from django.test import TestCase
import os
from Classes.functions import createCourse, setCourseId, setCourseName, setCourseSchedule, setCourseCredits
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()

from project_app.models import Course


class MyTestCase(TestCase):

    def test_courseIdexists(self):
        createCourse("361", "Software Engineering", "TR - 10:00", "3")
        self.assertEqual(createCourse("361", "Not Software Engineering", "MW - 12:00", "4"), "Course with that ID already exists")

    def test_courseCreated(self):
        createCourse("361", "Software Engineering", "TR - 10:00", "3")
        b = Course.objects.get(courseid="361")
        self.assertEqual("Software Engineering", b.coursename)
        self.assertEqual("TR - 10:00", b.courseschedule)
        self.assertEqual("3", b.coursecredits)

    def test_nocourseid(self):
        self.assertEqual(createCourse("", "Software Engineering", "TR @ 10:00 - 10:50", "3"), "Please fill out all required entries")

    def test_nocoursename(self):
        self.assertEqual(createCourse("361", "", "TR @ 10:00 - 10:50", "3"), "Please fill out all required entries")

    def test_nocourseschedule(self):
        self.assertEqual(createCourse("361", "Software Engineering", "", "3"), "Please fill out all required entries")

    def test_nocoursecredits(self):
        self.assertEqual(createCourse("361", "Software Engineering", "TR @ 10:00 - 10:50", ""), "Please fill out all required entries")



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
