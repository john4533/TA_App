from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import User

#from Classes.user import User



class TestDeleteAccount(TestCase):

    def setUp(self):
        self.user1= User("xyz@uwm.edu", "password123")
        self.user2= User("xyz@gmail.com","password123")
        self.user3= User("xyz@uwm.edu","pass")
        self.user4= User("aa@uwm.edu","123pass")
        self.user5= User("zz@uwm.edu","345two")

    def test_valid_user(self):
        self.assertEqual(True,self.deleteaccount(self.user1))

    def test_invalid_username(self):
        self.assertEqual(False, self.deleteaccount(self.user2))

    def test_invalid_password(self):
        self.assertEqual(False, self.deleteaccount(self.user3))

    def test_user_deleted1(self):
        self.assertEqual(True,self.deleteaccount(self.user4))
        c=False
        try:
             b=User.objects.get(username="aa@uwm.edu")
        except:
            c=True
            self.assertEqual(c,True)

    def test_user_deleted2(self):
        self.assertEqual(True, self.deleteaccount(self.user5))
        c = False
        try:
            b = User.objects.get(username="zz@uwm.edu")
        except:
            c = True
            self.assertEqual(c, True)

    def test_invalid_argument(self):
        with self.assertRaises(TypeError,"Not an user object") as context:
            self.admin.deleteaccount(" ")
            self.assertTrue("Invalid argument by the admin")

        with self.assertRaises(TypeError, "Not an user object") as context:
            self.admin.deleteaccount(None)
            self.assertTrue("Invalid argument by the admin")
