from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from Classes.functions import *

class UserTestCase(TestCase):

    def setUp(self):
        self.account1 = User.objects.create(username="xyz", password="password1", email="xyz@uwm.edu", role="Instructor")

#   CREATE ACCOUNT TESTS
    def test_useralreadyexists(self):
        self.assertEqual(createAccount("xyz", "password2", "abc@uwm.edu", "Supervisor"), "Please fill out all required entries")

    def test_usercreated(self):
        createAccount("user","xys","password2", "user@uwm.edu", "Instructor")
        b = User.objects.get(username="user")
        self.assertEqual("user@uwm.edu", b.email)
        self.assertEqual("password2", b.password)
        self.assertEqual("Instructor", b.role)

    def test_usercreatedwithextrainfo(self):
        m=createAccount("user", "xvy", "password2", "user@uwm.edu", "Instructor", "1-(123)-456-7890",
                      "20 Main Street", "123","T @ 3:00 - 3:50")
        b = User.objects.get(username="user")
        self.assertEqual("user@uwm.edu", b.email)
        self.assertEqual("password2", b.password)
        self.assertEqual("Instructor", b.role)
        self.assertEqual("1-(123)-456-7890", b.phone)
        self.assertEqual("20 Main Street", b.address)
        self.assertEqual("T @ 3:00 - 3:50", b.officehours)

    def test_nousername(self):
        self.assertEqual(createAccount("", "password1", "xyz@uwm.edu", "Instructor"), "Please fill out all required entries")

    def test_nopassword(self):
        self.assertEqual(createAccount("xyz", "", "xyz@uwm.edu", "Instructor"), "Please fill out all required entries")

    def test_noemail(self):
        self.assertEqual(createAccount("xyz", "password1", "", "Instructor"), "Please fill out all required entries")

    def test_norole(self):
        self.assertEqual(createAccount("xyz", "password1", "xyz@uwm.edu", ""), "Please fill out all required entries")


#   DELETE ACCOUNT TESTS
    def test_deletenoeusernameentered(self):
        self.assertEqual(deleteAccount(""), "Please enter a username")

    def test_deletenouserexists(self):
        self.assertEqual(deleteAccount("user2"), "User with that username does not exist")

    def test_deleteuser(self):
        self.assertEqual(self.account1.username, "xyz")
        self.assertEqual(deleteAccount("xyz"), "User with username xyz has been deleted")

#   LOGIN TESTS
    def test_invalidusername(self):
        self.assertFalse(login("abc", "password1"))

    def test_invalidpassword(self):
        self.assertFalse(login("xyz", "password2"))

    def test_validlogin(self):
        self.assertTrue(login("xyz", "password1"))

