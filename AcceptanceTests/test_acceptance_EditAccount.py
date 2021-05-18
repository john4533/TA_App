from django.test import TestCase, Client
from project_app.models import User, Course, Section, TA

class TestEditAccount(TestCase):

    def setUp(self):
        self.loginuser = User.objects.create(username="user23", name="user23", password="123", email="nub@uwm.edu",
                                             address="address",role="Supervisor", officehoursDays="M",
                                             officehoursEnd="12:00", officehoursStart="11:00", skills="skills")
        self.ta = User.objects.create(username="user3", name="user3", password="123", email="nub@uwm.edu",
                                      role="TA")
    def test_EditAccount_personal(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/editAccount/", {"update_account": "user23", "name": "user24", "password": "1234", "address": "address2",
                                                      "phone": "123-456-7890", "officenumber": "room",
                                                      "officehoursStart": "13:00", "officehoursEnd": "14:00",
                                                      "selectedDays": "Tuesday", "skills": "skillz" })
        self.assertEqual(response.url, '/Account/')

    def test_EditAccount_other(self):
        response = self.client.post("/", {"name": "user23", "password": "123"})
        self.assertEqual(response.url, '/Home/')
        response = self.client.post("/editAccount/", {"update_account": "user3", "name": "user24", "password": "1234",
                                                      "address": "address2",
                                                      "phone": "123-456-7890", "officenumber": "room",
                                                      "officehoursStart": "13:00", "officehoursEnd": "14:00",
                                                      "selectedDays": "Tuesday", "skills": "skillz"})
        self.assertEqual(response.url, '/AccountDisplay/')