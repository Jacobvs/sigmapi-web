from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from apps.Scholarship.models import TrackedUser, StudyHoursRecord, AcademicResource, LibraryItem

class StudyHoursTest(TestCase):
    fixtures = ["dev_data"]

    def setUp(self):
        self.userA = User.objects.get(username='brother')
        self.userB = User.objects.get(username='prchair')
        self.chair = User.objects.get(username='scholarshipchair')

        TrackedUser.objects.create(user=self.userA, number_of_hours=10)

        self.client = Client()
        self.client.force_login(self.chair)

    def test_track_new_user(self):
        """
        Test if a new user correctly becomes a TrackedUser
        
        This was the first test ever written for this site
        after close to 6 years of operation `this_is_fine.png`
        """
        # Ensure test user is not in the set already
        self.assertEqual(TrackedUser.objects.all().count(), 1)
        self.assertEqual(TrackedUser.objects.all().first().user, self.userA)

        path = reverse('scholarship-update_requirements')

        self.client.post(path, {
            "user": self.userB.id,
            'number_of_hours': 42,
        })

        # Check that test user is now in set
        self.assertEqual(TrackedUser.objects.all().count(), 2)
        self.assertTrue(TrackedUser.objects.get(user=self.userB))

    def test_reject_alumni_addition(self):
        """
        Ensure that an alumni can't
        get assigned study hours
        """
        path = reverse('scholarship-update_requirements')
        alumni = User.objects.get(username='alumni')

        r = self.client.post(path, {
            "user": alumni.id,
            "number_of_hours": 22
        })

        self.assertEqual(TrackedUser.objects.all().count(), 1)

    def test_fake_user_addition(self):
        """
        Test a non existant user id
        """
        path = reverse('scholarship-update_requirements')

        self.client.post(path, {
            "user": 0,
            "number_of_hours": 12,
        })

        self.assertEqual(TrackedUser.objects.all().count(), 1)