import unittest
import os
from Classes.course import Course
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from project_app.models import Users

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

