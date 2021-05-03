from django.test import TestCase, Client
from project_app.models import User, Course


class AccountDisplayTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="instructor1", name="kum", password="password", email="instructor@uwm.edu", role="Instructor",
                                        phone="123-456-7890", address="12 Main Street")
    def test_deleteuser(self):
        self.assertEqual(len(list(User.objects.all())), 1)
        response = self.client.post("/AccountDisplay/", {"delete_account": "instructor1"})
        self.assertEqual(len(list(User.objects.all())), 0)
        self.assertEqual(response.context["delete_message"], "User with username instructor1 has been deleted")

    def test_adduser(self):
        response = self.client.post("/AccountDisplay/", {"register_account": "register_account"})
        self.assertEqual(response.url, "/RegisterAccount/")
