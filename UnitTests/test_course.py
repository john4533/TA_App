import unittest
import os
from Classes.functions import createCourse, setCourseId, setCourseName, setCourseSchedule, setCourseCredits
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import Users, Course

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_nocourseid(self):
        with self.assertRaises(TypeError, msg="Need to input Course ID") as context:
            a = createCourse(None, "Software Engineering", "TR - 10:00", "3")

    def test_nocoursename(self):
        with self.assertRaises(TypeError, msg="Need to input Course name") as context:
            a = createCourse("361", None, "TR - 10:00", "3")

    def test_nocourseschedule(self):
        with self.assertRaises(TypeError, msg="Need to input Course schedule") as context:
            a = createCourse("361", "Software Engineering", None, "3")

    def test_nocoursecredits(self):
        with self.assertRaises(TypeError, msg="Need to input Course schedule") as context:
            a = createCourse("361", "Software Engineering", "TR - 10:00", None)

    def test_courseCreated(self):
        a = createCourse("361", "Software Engineering", "TR - 10:00", "3")
        b = Course.objects.get(courseid="361")
        self.assertEqual("Software Engineering", b.coursename)
        self.assertEqual("TR - 10:00", b.courseschedule)
        self.assertEqual("3", b.coursecredits)

    def test_courseIdexists(self):
        a = createCourse("361", "Software Engineering", "TR - 10:00", "3")
        with self.assertRaises(TypeError, msg="Course with that ID already exists") as context:
            b = createCourse("361", "Not Software Engineering", "MW - 12:00", "4")

    def test_courseIdupdated(self):
        a = createCourse("361", "Software Engineering", "TR - 10:00", "3")
        setCourseId("362", "361")
        b = Course.objects.get(courseid="362")
        self.assertEqual("Software Engineering", b.coursename)
        self.assertEqual("TR - 10:00", b.courseschedule)
        self.assertEqual("3", b.coursecredits)

    def test_courseNameupdated(self):
        a = createCourse("361", "Software Engineering", "TR - 10:00", "3")
        setCourseName("Not Software Engineering", "361")
        b = Course.objects.get(courseid="361")
        self.assertEqual("Not Software Engineering", b.coursename)

    def test_courseScheduleupdated(self):
        a = createCourse("361", "Software Engineering", "TR - 10:00", "3")
        setCourseSchedule("MW - 12:00", "361")
        b = Course.objects.get(courseid="361")
        self.assertEqual("MW - 12:00", b.courseschedule)

    def test_courseCreditsupdated(self):
        a = createCourse("361", "Software Engineering", "TR - 10:00", "3")
        setCourseCredits("4", "361")
        b = Course.objects.get(courseid="361")
        self.assertEqual("4", b.coursecredits)
