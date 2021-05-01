from django.test import TestCase
import os
from Classes.functions import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()


class CourseTestCase(TestCase):

#   CREATE COURSE TESTS
    def test_courseIdexists(self):
        Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        self.assertEqual(createCourse("337", "Software Engineering", "3"), "Course with that ID already exists")

    def test_courseCreated(self):
        createCourse("361", "Software Engineering", "3")
        b = Course.objects.get(courseid="361")
        self.assertEqual("Software Engineering", b.name)
        self.assertEqual("3", b.credits)

    def test_nocourseid(self):
        self.assertEqual(createCourse("", "Software Engineering", "3"), "Please fill out all required entries")

    def test_nocoursename(self):
        self.assertEqual(createCourse("361", "", "3"), "Please fill out all required entries")


    def test_nocoursecredits(self):
        self.assertEqual(createCourse("361", "Software Engineering", ""), "Please fill out all required entries")



#   DELETE COURSE TESTS
    def test_deletenocourseidentered(self):
        self.assertEqual(deleteCourse(""), "Please enter a course ID")

    def test_deletenocourseexists(self):
        self.assertEqual(deleteCourse("361"), "Course with that ID does not exist")

    def test_deletecourse(self):
        course1 = Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        self.assertEqual(course1.courseid, "337")
        self.assertEqual(deleteCourse("337"), "Course with ID 337 has been deleted")

#   GET COURSES TESTS
    def test_getCourses_noCourses(self):
        self.assertEqual(getCourses(), {})

    def test_getCourses_noLabs(self):
        course1 = Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        self.assertEqual(getCourses(), {course1: []})

    def test_getCourses_success(self):
        course1 = Course.objects.create(courseid="337",name="Systems Programming",credits="3")
        section= Section.objects.create(course=course1, sectionid="901", type="Lab 1",schedule="T @ 11:00 - 12:50")
        self.assertEqual(getCourses(), {course1: [section]})

    # ASSIGN COURSES (ASSUMPTION: USERS AND COURSES ARE VALID)
    def test_Invalid_user_assigned_course(self):
          user1 = createAccount("zyx", "123", "zyx@uwm.edu", "Supervisor", "414-243-9503", "address", "officehours")
          user2 = createAccount("z", "123", "abc@uwm.edu", "TA", "414-243-9503", "address", "officehours")
          course1 = createCourse("1", "y", "3")
          self.assertEqual("Course cannot be assigned to Supervisor", assignUser(user1, course1))
          self.assertEqual("Course cannot be assigned to TA", assignUser(user2, course1))

    def test_valid_user_assigned_course(self):
         user2 = createAccount("a", "123", "a@uwm.edu", "Instructor", "414-243-9503", "address", "officehours")
         user3 = createAccount("b", "123", "b@uwm.edu", "Instructor", "414-243-9503", "address", "officehours")
         course2 = createCourse("2", "b", "3")
         course3 = createCourse("3", "c", "3")
         self.assertEqual("Course has been assigned", assignUser(user2, course2))
         self.assertEqual("Course has been assigned", assignUser(user3, course3))

    def test_multiple_courses_assigned(self):
         user4 = createAccount("c", "123", "c@uwm.edu", "Instructor", "414-243-9503", "address", "officehours")
         course4 = createCourse("4", "c", "3")
         course5 = createCourse("5", "d", "3")
         course6 = createCourse("6", "f", "3")
         self.assertEqual("Course has been assigned", assignUser(user4, course4))
         self.assertEqual("Course has been assigned", assignUser(user4, course5))
         self.assertEqual("Course has been assigned", assignUser(user4, course6))

    def test_instructor_already_assigned(self):
        user5 = createAccount("d", "123", "c@uwm.edu", "Instructor", "414-243-9503", "address", "officehours")
        user6 = createAccount("e", "123", "c@uwm.edu", "Instructor", "414-243-9503", "address", "officehours")
        course7 = createCourse("1", "a", "2")
        assignUser(user5, course7)
        self.assertEquals(assignUser(user6, course7), "Course already has an instructor assigned to it")

    def test_invalid_arguments_assigned(self):
        testuser = createAccount("testuser", "test123", "test@uwm.edu", "Instructor", "123-456-7890", "testaddress", "testhours")
        testcourse = createCourse("123", "test", "1 to 3")

        try:
            assignUser("", "")
        except ValueError:
            print("Invalid arguments")

        try:
            assignUser(None, None)
        except ValueError:
            print("Invalid arguments")

        try:
            assignUser(testuser, None)
        except ValueError:
            print("Invalid course argument")

        try:
            assignUser(testuser, "")
        except ValueError:
            print("Invalid course argument")

        try:
            assignUser(None, testcourse)
        except ValueError:
            print("Invalid user argument")

        try:
            assignUser("", testcourse)
        except ValueError:
            print("Invalid user argument")


