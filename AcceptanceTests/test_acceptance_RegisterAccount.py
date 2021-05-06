from django.test import TestCase, Client
from project_app.models import User


class SupAccountsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="user",name="user1", password="password", email="user@uwm.edu", role="supervisor")
        self.loginuser= User.objects.create(username="user23", name="user23", password="123",email="nub@uwm.edu",role="supervisor")
    def test_accountExists(self):
        response = self.client.post("/RegisterAccount/", {"username": self.user.username, "name":"user1", "password": self.user.password,
                                    "email": self.user.email, "role": self.user.role})
        self.assertEqual(response.context["message"], "User with that username already exists", msg="User created twice")

    def test_createAccount(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url,'/Home/')
        response = self.client.post("/RegisterAccount/", {"username": "user1","name":"kad", "password": "password1",
                                                          "email": "user1@uwm.edu", "role": "instructor", "phone": "",
                                                          "address": "","officenumber":"23", "officehours": "","skills":""})
        self.assertEqual(response.url, "/AccountDisplay/")

        response = self.client.post("/RegisterAccount/", {"username": "user2", "name":"mo","password": "password1",
                                    "email": "user1@uwm.edu", "role": "instructor", "phone": "", "address": "","officenumber":"124", "officehours": "","skills":""}, follow=True)
        self.assertEqual(len(response.context["accounts"]), 4)

    def test_createAccountwithfullinfo(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')

        response = self.client.post("/RegisterAccount/", {"username": "user1","name": "4er","password": "password1",
                                    "email": "user1@uwm.edu", "role": "instructor", "phone": "1-(123)-456-7890",
                                    "address": "20 Main Street","officenumber":"43", "officehours": "T @ 3:00 - 3:50","skills":""})
        self.assertEqual(response.url, '/AccountDisplay/')

        response = self.client.post("/RegisterAccount/", {"username": "user2", "name": "4wer","password": "password1",
                                                          "email": "user1@uwm.edu", "role": "instructor",
                                                          "phone": "1-(123)-456-7890",
                                                          "address": "20 Main Street","officenumber":"43",
                                                          "officehours": "T @ 3:00 - 3:50","skills":""}, follow=True)
        self.assertEqual(len(response.context["accounts"]), 4)

    def test_emptyUsername(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterAccount/", {"username": "","name":"Bb", "password": "password1",
                                    "email": "user1@uwm.edu", "role": "instructor"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty username, user created without username")

    def test_emptyPassword(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterAccount/", {"username": "user1","name":"cc", "password": "",
                                    "email": "user1@uwm.edu", "role": "instructor"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty password, user created without password")

    def test_emptyEmail(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterAccount/", {"username": "user1","name":"usewe","password": "password1",
                                    "email": "", "role": "instructor"})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty email, user created without email")

    def test_emptyRole(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/RegisterAccount/", {"username": "user1","name":"WW", "password": "password1",
                                    "email": "user1@uwm.edu", "role": ""})
        self.assertEqual(response.context["message"], "Please fill out all required entries", msg="Empty role, user created without role")