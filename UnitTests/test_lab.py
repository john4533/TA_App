from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from Classes.functions import *

class LabTestCase(TestCase):

    def setUp(self):
        self.course1 = Course.objects.create(courseid="337", coursename="Systems Programming", courseschedule="TR @ 1:00 - 1:50", coursecredits="3")
        self.lab1 = Lab.objects.create(course=self.course1, labid="902", labname="Software Engineering Lab 2", labschedule="R @ 11:00 - 12:50")

#   CREATE COURSE TESTS
    def test_labIdexists(self):
        self.assertEqual(createLab(self.course1, "902", "Software Engineering Lab 1", "T @ 11:00 - 12:50"),
                         "Lab with that ID already exists")

    def test_labCreated(self):
        createLab(self.course1, "901", "Software Engineering Lab 1", "T @ 11:00 - 12:50")
        b = Lab.objects.get(labid="901")
        self.assertEqual("Software Engineering Lab 1", b.labname)
        self.assertEqual("T @ 11:00 - 12:50", b.labschedule)

    def test_nolabid(self):
        self.assertEqual(createLab(self.course1, "", "Software Engineering Lab 1", "R @ 11:00 - 12:50"),
                         "Please fill out all required entries")

    def test_nolabename(self):
        self.assertEqual(createLab(self.course1, "901", "", "R @ 11:00 - 12:50"), "Please fill out all required entries")

    def test_nolabschedule(self):
        self.assertEqual(createLab(self.course1, "901", "Software Engineering Lab 1", ""), "Please fill out all required entries")


#   DELETE LAB TESTS
    def test_deletenolabidentered(self):
        self.assertEqual(deleteLab(""), "Please enter a lab ID")

    def test_deletenolabexists(self):
        self.assertEqual(deleteLab("901"), "Lab with that ID does not exist")

    def test_deletelab(self):
        self.assertEqual(self.lab1.labid, "902")
        self.assertEqual(deleteLab("902"), "Lab with ID 902 has been deleted")
