import unittest
import os
from Classes.user import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import Users

class UserTestCase(unittest.TestCase):

    def test_init(self):
        a = User("xyz@uwm.edu", "password1")
        self.assertEqual(a.name, "xyz@uwm.edu")
        self.assertEqual(a.password, "password1")

    def test_noname(self):
        with self.assertRaises(TypeError, msg="Empty Username") as context:
            b = User("", "password1")

    def test_nopassword(self):
        with self.assertRaises(TypeError, msg="Empty Password") as context:
            b = User("xyz@uwm.edu", "")


    def test_useralreadyexists(self):
        a = User("xyz@uwm.edu", "password1")
        a.create_user()
        with self.assertRaises(TypeError, msg="User already exists") as context:
            b = User("xyz@uwm.edu", "password2")
            b.create_user()

    def test_usercreated(self):
        a = User("xyz@uwm.edu", "password1")
        self.assertEqual(a.create_user(), None)
        b = Users.objects.get(username=a.name)
        self.assertEqual(a.name,
                         b.name)  ## We have several attributes for user database, so I dont know how will li[0] store all those attributes
        self.assertEqual(a.password, b.password)

    def test_nouwm(self):
        with self.assertRaises(TypeError, msg="No @uwm.edu") as context:
            a = User.create_user("xyz@gmail.com", "password1")

    def invalid_username(self):
        a = User("xyz@uwm.edu", "password1")
        self.assertNotEqual(a.name, "xyzz@uwm.edu")

    def invalid_password(self):
        self.assertNotEqual(Users.objects.get(name="xyz@uwm.edu"), "password2")

    def valid_login(self):
        pass




