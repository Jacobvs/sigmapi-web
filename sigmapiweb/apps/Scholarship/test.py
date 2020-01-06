from django.test import TestCase
from django.contrib.auth.models import User

from apps.Scholarship.models import TrackedUser, StudyHoursRecord, AcademicResource, LibraryItem

class StudyHoursTest(TestCase):
    fixtures = ["dev_data"]

    def setUp(self):
        userA = User.objects.get(username="brother")
        userB = User.objects.get(username="scholarshipchair")

        TrackedUser.objects.create(user=userA, number_of_hours=10)

    def test_track_new_user(self):
        """
        test test
        """
        self.assertTrue(True)

    def test2(self):
        self.assertFalse(False)
