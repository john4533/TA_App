from django.test import TestCase, Client
from project_app.models import User, Course


class AccountTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="supervisor", password="supervisor", email="supervisor@uwm.edu", role="Supervisor",
                            phone="123-456-7890", address="12 Main Street")

    def test_namedisplay(self):
        response = self.client.post("/", {"name": "supervisor", "password": "supervisor"})
        self.assertEqual(response.url, "/SupHome/", msg="Valid Login redirects the user to the incorrect url")

        response = self.client.post("/Account/", {"user": self.user})
        self.assertEqual(response.context["user"], "supervisor")


