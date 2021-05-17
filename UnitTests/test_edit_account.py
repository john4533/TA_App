from django.test import TestCase
import os
from Classes.functions import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
import datetime


class EditAccountTest(TestCase):

    def setUp(self):
        self.test_Ins = User.objects.create(username="testInsUser", name="testInsName", password="123",
                                            email="testIns@uwm.edu", role="Instructor", phone="123-456-7890",
                                            address="testInsAddress", officenumber="E252", officehoursStart="10:00",
                                            officehoursEnd="10:50", officehoursDays="MT", skills="skills")
    def test_editAccount(self):
        self.assertEqual(editAccount("testInsUser", "newName", "321", "newAddress", "098-765-4321", "newRoom", "11:00", "12:00",
                    ["Wednesday", "Thursday"], "skillz"), "")
        editAccount("testInsUser", "newName", "321", "newAddress", "098-765-4321", "newRoom", "11:00", "12:00",
                    ["Wednesday", "Thursday"], "skillz")
        a = User.objects.get(username="testInsUser")
        self.assertEqual("newName", a.name)
        self.assertEqual("321", a.password)
        self.assertEqual("098-765-4321", a.phone)
        self.assertEqual("newRoom", a.officenumber)
        self.assertEqual(datetime.time(11, 0), a.officehoursStart)
        self.assertEqual(datetime.time(12, 0), a.officehoursEnd)
        self.assertEqual("WR", a.officehoursDays)
        self.assertEqual("skillz", a.skills)


