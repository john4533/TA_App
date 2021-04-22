import unittest
import os
from Classes.user import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import User, Course
from Classes.functions import *

class UserTestCase(unittest.TestCase):

    def test_useralreadyexists(self):
        createAccount("xyz", "password1", "xyz@uwm.edu", "instructor")
        with self.assertRaises(TypeError, msg="User with that email already exists") as context:
            createAccount("abc", "password2", "xyz@uwm.edu", "instructor")

    def test_usercreated(self):
        createAccount("xyz", "password1", "xyz@uwm.edu", "instructor")
        b = User.objects.get(email="xyz@uwm.edu")
        self.assertEqual("xyz", b.name)
        self.assertEqual("password1", b.password)
        self.assertEqual("xyz@uwm.edu", b.email)
        self.assertEqual("instructor", b.role)


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