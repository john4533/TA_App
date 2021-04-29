from django.test import TestCase
import os
from Classes.functions import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()



class EditAccountTest(TestCase):

    def setUp(self):
        user1=createAccount("b", "123","wer@uwm.edu","Supervisor", phone="123-421-4123", address="xyz", officehours="xy:y")


