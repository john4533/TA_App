from django.test import TestCase
import os
from Classes.user import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import User, Course
from Classes.functions import *

class UserTestCase(TestCase):

#   CREATE ACCOUNT TESTS
    def test_useralreadyexists(self):
        createAccount("xyz", "password1", "xyz@uwm.edu", "instructor")
        self.assertEqual(createAccount("abc", "password2", "xyz@uwm.edu", "supervisor"), "User with that email already exists")

    def test_usercreated(self):
        createAccount("xyz", "password1", "xyz@uwm.edu", "instructor")
        b = User.objects.get(email="xyz@uwm.edu")
        self.assertEqual("xyz", b.username)
        self.assertEqual("password1", b.password)
        self.assertEqual("instructor", b.role)

    def test_nousername(self):
        self.assertEqual(createAccount("", "password1", "xyz@uwm.edu", "instructor"), "Please fill out all required entries")

    def test_nopassword(self):
        self.assertEqual(createAccount("xyz", "", "xyz@uwm.edu", "instructor"), "Please fill out all required entries")

    def test_noemail(self):
        self.assertEqual(createAccount("xyz", "password1", "", "instructor"), "Please fill out all required entries")

    def test_norole(self):
        self.assertEqual(createAccount("xyz", "password1", "xyz@uwm.edu", ""), "Please fill out all required entries")


# LOGIN TESTS
    def test_invalidusername(self):
        createAccount("xyz", "password1", "xyz@uwm.edu", "instructor")
        self.assertFalse(login("abc", "password1"))

    def test_invalidpassword(self):
        createAccount("xyz", "password1", "xyz@uwm.edu", "instructor")
        self.assertFalse(login("xyz", "password2"))

    def test_validlogin(self):
        createAccount("xyz", "password1", "xyz@uwm.edu", "instructor")
        self.assertTrue(login("xyz", "password1"))


    # def test_init(self):
    #     a = User("xyz@uwm.edu", "password1")
    #     self.assertEqual(a.name, "xyz@uwm.edu")
    #     self.assertEqual(a.password, "password1")
    #
    # def test_noname(self):
    #     with self.assertRaises(TypeError, msg="Empty Username") as context:
    #         b = User("", "password1")
    #
    # def test_nopassword(self):
    #     with self.assertRaises(TypeError, msg="Empty Password") as context:
    #         b = User("xyz@uwm.edu", "")


    # def test_nouwm(self):
    #     with self.assertRaises(TypeError, msg="No @uwm.edu") as context:
    #         a = User.create_user("xyz@gmail.com", "password1")