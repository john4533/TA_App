from django.test import TestCase, Client
from project_app.models import User


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(username="Charlie", password="Password123", email="charlie@uwm.edu", role="TA")
        self.user2 = User.objects.create(username="Bob", password="Password123", email="bob@uwm.edu", role="Supervisor")
        self.user3 = User.objects.create(username="Joe", password="Password123", email="joe@uwm.edu", role="Instructor")

    # def test_existingUser_ValidLoginTA(self):
    #     response = self.client.post("/", {"name": "Charlie", "password": "Password123"})
    #     self.assertEqual(response.url, "/TAHome/", msg="Valid Login redirects the user to the incorrect url")

    def test_existingUser_ValidLoginSupervisor(self):
        response = self.client.post("/", {"name": "Bob", "password": "Password123"})
        self.assertEqual(response.url, "/SupHome/", msg="Valid Login redirects the user to the incorrect url")

    # def test_existingUser_ValidLoginInstructor(self):
    #     response = self.client.post("/", {"name": "Joe", "password": "Password123"})
    #     self.assertEqual(response.url, "/InsHome/", msg="Valid Login redirects the user to the incorrect url")

    def test_invalidPassword(self):
        response = self.client.post("/", {"name": "Charlie", "password": "Password124"})
        self.assertEqual(response.context["message"], "Information is incorrect", msg="Invalid login, incorrect password passes")

    def test_usernameDNE(self):
        response = self.client.post("/", {"name": "Bryce", "password": "Password123"})
        self.assertEqual(response.context["message"], "Information is incorrect", msg="Invalid login, incorrect username passes")
