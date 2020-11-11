from django.test import Client, TestCase
from django.urls import reverse

"""
Unit tests for correct HTTP response of all public site pages 
"""

class PublicViewTests(TestCase):

    print("->Testing Public Site Pages Correct Response")

    fixtures = ['dev_data']

    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        """
        Test if Home Page renders
        """
        # pub-index here is the name of the url to get the view for, defined in
        # /pubsite/urls.py 
        response = self.client.get(reverse('pub-index'))
        self.assertEqual(response.status_code, 200)

    def test_brothers_page(self):
        """
        Test if Brother Page renders
        """
        # The view/url/template for the brothers page is actually defined in the
        # UserInfo/ directory. Url name is userinfo-users.
        response = self.client.get(reverse('userinfo-users'))
        print("NUMBER OF BROTHER GROUPS: ", len(response.context['brother_groups']))
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        """
        Test if About Page renders
        """
        response = self.client.get(reverse('pub-about'))
        self.assertEqual(response.status_code, 200)

    def test_service_page(self):
        """
        Test if Service and Activities Page renders with /service path
        """
        response = self.client.get(reverse('pub-service'))
        # Gets a 302 status code that means it is correctly redirecting
        self.assertEqual(response.status_code, 302)

    def test_activities_page(self):
        """
        Test if Service and Activities Page renders with /activities path
        """
        response = self.client.get(reverse('pub-activities'))
        self.assertEqual(response.status_code, 200)

    def test_log_in_page(self):
        """
        Test if Log In Page renders
        """
        response = self.client.get(reverse('pub-login'))
        self.assertEqual(response.status_code, 200)

    def test_rush_page(self):
        """
        Test if Rush Page renders
        """
        response = self.client.get(reverse('pub-rush'))
        self.assertEqual(response.status_code, 200)