from django.test import TestCase
from project_app.models import Users
import unittest

# Unittests
class TestUserCreate(unittest.TestCase):

    def setUp(self):
        self.user1 = Users.objects.create(name="xyz@uwm.edu", password="password1")

    def test_useralreadyexists(self):
        a = Users.objects.create(name="xyz@uwm.edu", password="password1")
        with self.assertRaises(TypeError, msg="User already exists"):
            b = Users.objects.create("xyz@uwm.edu", "password2")

    def test_usercreated(self):
        pass


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        pass



