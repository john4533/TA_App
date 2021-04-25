from django.test import TestCase, Client
from project_app.models import User, Course


class SupAccountsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="user", password="password", email="user@uwm.edu", role="supervisor")

    def test_accountExists(self):
        response = self.client.post("/RegisterAccount/", {"username": self.user.username, "password": self.user.password,
                                    "email": self.user.email, "role": self.user.role})
        self.assertEqual(response.context["message"], "User with that email already exists", msg="User created twice")

    def test_createAccount(self):
        response = self.client.post("/RegisterAccount/", {"username": "user1", "password": "password1",
                                    "email": "user1@uwm.edu", "role": "instructor"})
        last_index = len(response.context["accounts"]) - 1
        self.assertEqual(response.context["accounts"][last_index].username, "user1")
        self.assertEqual(response.context["accounts"][last_index].password, "password1")
        self.assertEqual(response.context["accounts"][last_index].email, "user1@uwm.edu")
        self.assertEqual(response.context["accounts"][last_index].role, "instructor")

    def test_emptyUsername(self):
        response = self.client.post("/RegisterAccount/", {"username": "", "password": "password1",
                                    "email": "user1@uwm.edu", "role": "instructor"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty username, user created without username")

    def test_emptyPassword(self):
        response = self.client.post("/RegisterAccount/", {"username": "user1", "password": "",
                                    "email": "user1@uwm.edu", "role": "instructor"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty password, user created without password")

    def test_emptyEmail(self):
        response = self.client.post("/RegisterAccount/", {"username": "user1", "password": "password1",
                                    "email": "", "role": "instructor"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty email, user created without email")

    def test_emptyRole(self):
        response = self.client.post("/RegisterAccount/", {"username": "user1", "password": "password1",
                                    "email": "user1@uwm.edu", "role": ""})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty role, user created without role")

