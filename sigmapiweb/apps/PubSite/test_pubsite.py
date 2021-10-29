from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from datetime import date
import sigmapiweb.apps.UserInfo


class PublicViewTests(TestCase):
    fixtures = ["dev_data"]

    def setUp(self):
        self.client = Client()
        self.group = Group.objects

    def test_home_page(self):
        """
        Test if the home page renders
        """
        # pub-index here is the name of the url to get the view for, defined in
        # /pubsite/urls.py
        response = self.client.get(reverse("pub-index"))
        self.assertEqual(response.status_code, 200)

    def test_brothers_page(self):
        # The view/url/template for the brothers page is actually defined in the
        # UserInfo/ directory. Url name is userinfo-users.
        response = self.client.get(reverse("userinfo-users"))
        # look at the actual data and build dict of how many brothers should be in each section
        # also look at number of groups to make sure they match?
        returned_num_brothers = {}
        names_in_EC = {}  # so we don't count this number later on
        grad_years = {}

        today = date.today()
        curr_year = today.year
        curr_month = today.month
        # setup for seniors graduating in the current calendar year, and grad students being > that.
        # TODO update this to how we do it on site
        if curr_month < 7:
            senior_year = curr_year
        else:
            senior_year = curr_year + 1
        class_to_year_mappings = {
            "Graduate Students": senior_year - 1,
            "Seniors": senior_year,
            "Juniors": senior_year + 1,
            "Sophomores": senior_year + 2,
            "Freshmen": senior_year + 2,
        }

        # loop through the webpage response to collect num of brothers in each group
        for brother_group in response.context["brother_groups"]:
            # check size of this brother group
            print("Length of group:", len(brother_group["brothers"]))
            returned_num_brothers[brother_group["group_title"]] = len(
                brother_group["brothers"]
            )
            # if brothers are in the EC, they shouldn't go into the counts for those groups
            if brother_group["group_title"] == "Executive Council":
                for bro in brother_group["brothers"]:
                    if bro:
                        try:
                            names_in_EC[bro.first_name + bro.last_name] = 1
                        except User.userinfo.RelatedObjectDoesNotExist:
                            pass
                            # print("No info")

        # loop through brothers in the db and collect graduation years. Only get them if they aren't in the EC
        all_brothers_db = User.objects.all()
        for brother in all_brothers_db:
            try:
                user_info = brother.userinfo
                if (brother.first_name + brother.last_name) not in names_in_EC:
                    grad_year = user_info.graduationYear
                    if grad_year < senior_year:
                        grad_year = senior_year - 1
                    if user_info.graduationYear in grad_years:
                        grad_years[grad_year] += 1
                    else:
                        grad_years[grad_year] = 1
                else:
                    if user_info.graduationYear not in grad_years:
                        grad_years[user_info.graduationYear] = 0
            except User.userinfo.RelatedObjectDoesNotExist:
                pass

        # print(returned_num_brothers)
        # print(grad_years)

        # TODO: broken
        """
        for key in class_to_year_mappings:
            try:
                self.assertEqual(
                    grad_years[class_to_year_mappings[key]], returned_num_brothers[key]
                )
            except KeyError as e:
                print("Year not in any user infos: ", e)
                
        """

        self.assertEqual(response.status_code, 200)
