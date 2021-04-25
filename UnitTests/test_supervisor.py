from django.test import TestCase
import os
from Classes.supervisor import Supervisor
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import User

class MyTestCase(TestCase):
    pass
    # def test_something(self):
    #     self.assertEqual(True, False)
