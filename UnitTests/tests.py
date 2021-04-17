import unittest
import os
from Classes.functions import *
from Classes.supervisor import Supervisor
from Classes.user import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import Users, Course, Lab

if __name__ == '__main__':
    unittest.main()


class TestDeleteAccount(unittest.TestCase):
    def setUp(self):
        self.user1= User("xyz@uwm.edu", "password123")
        self.user2=User("xyz@gmail.com","password123")
        self.user3=User("xyz@uwm.edu","pass")
        self.admin=Supervisor("abc@uwm.edu","123")

    def test_valid_user(self):
        self.assertEqual(True,self.admin.deleteaccount(self.user1))

    def test_invalid_username(self):
        self.assertEqual(False, self.admin.deleteaccount(self.user2))

    def test_invalid_password(self):
        self.assertEqual(False, self.admin.deleteaccount(self.user3))

    def test_invalid_argument(self):
        with self.assertRaises(TypeError,"Not an user object") as context:
            self.admin.deleteaccount(" ")
            self.assertTrue("Invalid argument by the admin")

        with self.assertRaises(TypeError, "Not an user object") as context:
            self.admin.deleteaccount(None)
            self.assertTrue("Invalid argument by the admin")

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

class TestDeleteAccount(unittest.TestCase):

    def setUp(self):
        self.user1= User("xyz@uwm.edu", "password123")
        self.user2=User("xyz@gmail.com","password123")
        self.user3=User("xyz@uwm.edu","pass")

    def test_valid_user(self):
        self.assertEqual(True,self.deleteaccount(self.user1))

    def test_invalid_username(self):
        self.assertEqual(False, self.deleteaccount(self.user2))

    def test_invalid_password(self):
        self.assertEqual(False, self.deleteaccount(self.user3))

    def test_invalid_argument(self):
        with self.assertRaises(TypeError,"Not an user object") as context:
            self.admin.deleteaccount(" ")
            self.assertTrue("Invalid argument by the admin")

        with self.assertRaises(TypeError, "Not an user object") as context:
            self.admin.deleteaccount(None)
            self.assertTrue("Invalid argument by the admin")