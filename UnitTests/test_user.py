from django.test import TestCase
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django

django.setup()
from Classes.functions import *

import datetime

class UserTestCase(TestCase):

    def setUp(self):
        self.account1 = User.objects.create(username="user1", name="name1", password="password1", email="user1@uwm.edu",
                                            role="Instructor", phone="123-456-7890", address="address1",
                                            officenumber="room1", officehoursStart="11:00:00", officehoursEnd="12:00:00",
                                            officehoursDays="MT", skills="skills1")

    #   CREATE ACCOUNT TESTS
    def test_useralreadyexists(self):
        self.assertEqual(createAccount("user1", "name2", "password2", "user2@uwm.edu", "Supervisor", "123-456-7890",
                                       "address2", "room2", "11:00:00", "12:00:00", ["Monday", "Tuesday"], "skills2"),
                         "User with that username already exists")

    def test_usercreated(self):
        createAccount("user2", "name2", "password2", "user2@uwm.edu", "Instructor", "123-456-7890", "address2", "room2",
                      "11:00:00", "12:00:00", ["Monday", "Tuesday"], "skills2")
        b = User.objects.get(username="user2")
        self.assertEqual("name2", b.name)
        self.assertEqual("password2", b.password)
        self.assertEqual("user2@uwm.edu", b.email)
        self.assertEqual("Instructor", b.role)
        self.assertEqual("123-456-7890", b.phone)
        self.assertEqual("address2", b.address)
        self.assertEqual("room2", b.officenumber)
        self.assertEqual(datetime.time(11, 0), b.officehoursStart)
        self.assertEqual(datetime.time(12, 0), b.officehoursEnd)
        self.assertEqual("MT", b.officehoursDays)
        self.assertEqual("skills2", b.skills)

    def test_nousername(self):
        self.assertEqual(createAccount("", "password1", "xyz@uwm.edu", "Instructor"),
                         "Please fill out all required entries")

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
        self.assertEqual(self.account1.username, "user1")
        self.assertEqual(deleteAccount("user1"), "User with username user1 has been deleted")

    #   LOGIN TESTS
    def test_invalidusername(self):
        self.assertFalse(login("abc", "password1"))

    def test_invalidpassword(self):
        self.assertFalse(login("user1", "password2"))

    def test_validlogin(self):
        self.assertTrue(login("user1", "password1"))
