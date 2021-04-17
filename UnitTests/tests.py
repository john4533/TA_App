import unittest
import os
from Classes.functions import *
from Classes.supervisor import Supervisor
from Classes.user import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import Users, Course, Lab

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


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

