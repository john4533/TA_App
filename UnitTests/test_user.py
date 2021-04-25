from django.test import TestCase
import os
from Classes.user import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import User, Course
from Classes.functions import *

class UserTestCase(TestCase):

    def setUp(self):
        self.account1 = User.objects.create(username="xyz", password="password1", email="xyz@uwm.edu", role="Instructor")

#   CREATE ACCOUNT TESTS
    def test_useralreadyexists(self):
        self.assertEqual(createAccount("abc", "password2", "xyz@uwm.edu", "Supervisor"), "User with that email already exists")

    def test_usercreated(self):
        createAccount("user", "password2", "user@uwm.edu", "Instructor")
        b = User.objects.get(email="user@uwm.edu")
        self.assertEqual("user", b.username)
        self.assertEqual("password2", b.password)
        self.assertEqual("Instructor", b.role)

    def test_nousername(self):
        self.assertEqual(createAccount("", "password1", "xyz@uwm.edu", "Instructor"), "Please fill out all required entries")

    def test_nopassword(self):
        self.assertEqual(createAccount("xyz", "", "xyz@uwm.edu", "Instructor"), "Please fill out all required entries")

    def test_noemail(self):
        self.assertEqual(createAccount("xyz", "password1", "", "Instructor"), "Please fill out all required entries")

    def test_norole(self):
        self.assertEqual(createAccount("xyz", "password1", "xyz@uwm.edu", ""), "Please fill out all required entries")


#   DELETE ACCOUNT TESTS
    def test_deletenoemailentered(self):
        self.assertEqual(deleteAccount(""), "Please enter an email")

    def test_deletenocourseexists(self):
        self.assertEqual(deleteAccount("user2@uwm.edu"), "User with that email does not exist")

    def test_deletecourse(self):
        self.assertEqual(self.account1.email, "xyz@uwm.edu")
        self.assertEqual(deleteAccount("xyz@uwm.edu"), "User with email xyz@uwm.edu has been deleted")

# LOGIN TESTS
    def test_invalidusername(self):
        self.assertFalse(login("abc", "password1"))

    def test_invalidpassword(self):
        self.assertFalse(login("xyz", "password2"))

    def test_validlogin(self):
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