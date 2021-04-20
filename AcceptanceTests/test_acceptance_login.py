import unittest
from django.test import TestCase, Client
from project_app.models import Users


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = Users.objects.create(username="Charlie", password="Password123", email=None, role="TA", phone=None, address=None, officehours=None)
        self.user2 = Users.objects.create(username="Bob", password="Password123", email=None, role="Supervisor", phone=None, address=None, officehours=None)
        self.user3 = Users.objects.create(username="Joe", password="Password123", email=None, role="Instructor", phone=None, address=None, officehours=None)

    def test_existingUser_ValidLoginTA(self):
        response = self.client.post("/", {"name": "Charlie", "password": "Password123"})
        self.assertEqual(response.url, "/ta_home/", msg="Valid Login redirects the user to the incorrect url")

    def test_existingUser_ValidLoginSupervisor(self):
        response = self.client.post("/", {"name": "Bob", "password": "Password123"})
        self.assertEqual(response.url, "/sup_home/", msg="Valid Login redirects the user to the incorrect url")

    def test_existingUser_ValidLoginInstructor(self):
        response = self.client.post("/", {"name": "Joe", "password": "Password123"})
        self.assertEqual(response.url, "/ins_home/", msg="Valid Login redirects the user to the incorrect url")

    def test_invalidPassword(self):
        response = self.client.post("/", {"name": "Charlie", "password": "Password124"})
        self.assertEqual(response.context["message"], "information is incorrect", msg="Invalid login, incorrect password passes")

    def test_usernameDNE(self):
        response = self.client.post("/", {"name": "Bryce", "password": "Password123"})
        self.assertEqual(response.context["message"], "information is incorrect", msg="Invalid login, incorrect username passes")

if __name__ == '__main__':
    unittest.main()
