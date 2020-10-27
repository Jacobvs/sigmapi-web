from django.test import Client, TestCase
from django.urls import reverse

class PublicViewTests(TestCase):
    fixtures = ['dev_data']

    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        """
        Test if the home page renders
        """
        # pub-index here is the name of the url to get the view for, defined in
        # /pubsite/urls.py 
        response = self.client.get(reverse('pub-index'))
        self.assertEqual(response.status_code, 200)

    def test_brothers_page(self):
        # The view/url/template for the brothers page is actually defined in the
        # UserInfo/ directory. Url name is userinfo-users.
        response = self.client.get(reverse('userinfo-users'))
        print("NUMBER OF BROTHER GROUPS: ", len(response.context['brother_groups']))
        self.assertEqual(response.status_code, 200)