from django.test import TestCase, Client
from project_app.models import User
import unittest

# Unittests
class TestUserCreate(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(name="xyz@uwm.edu", password="password1")

    def test_useralreadyexists(self):
        with self.assertRaises(TypeError, msg="User already exists"):
            b = User.objects.create("xyz@uwm.edu", "password2")

    def test_usercreated(self):
        pass


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        pass



