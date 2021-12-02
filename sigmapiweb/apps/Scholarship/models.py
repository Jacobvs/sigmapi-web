"""
Models for Scholarship app.
"""
import datetime
import re

from django.contrib.auth.models import User
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import RegexValidator, validate_integer

from common.mixins import ModelMixin


def validate_stars(number):
    """
    Raises a validation error if the given number is <1 or >5.
    Arguments:
        number (int)
    """
    if number < 1:
        raise ValidationError("The stars given cannot be below 1.")
    elif number > 5:
        raise ValidationError("The stars given cannot be above 5.")


def validate_date(date):
    """
    Raises a validation error if the given date is in the future.

    Arguments:
        date (datetime)
    """
    if date > datetime.date.today():
        raise ValidationError("The date given cannot be in the future.")


def validate_number(number):
    """
    Raises a validation error if the given number is negative.

    Arguments:
        number (int)
    """
    if number < 0:
        raise ValidationError("The number given cannot be negative.")


def occurred_this_week(date):
    """
    Returns whether the given date occured within this week (starting Monday).

    Arguments:
        date (datetime)

    Returns: bool
    """
    one_week_delta = datetime.timedelta(days=7)
    today_date = datetime.date.today()
    today_date_weekday_number = today_date.weekday()
    beginning_of_week_monday = today_date - datetime.timedelta(
        days=today_date_weekday_number
    )
    next_monday = beginning_of_week_monday + one_week_delta

    return beginning_of_week_monday <= date < next_monday


class TrackedUser(ModelMixin, models.Model):
    """
    Model for a user who currently has their study hours tracked.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_hours = models.IntegerField(validators=[validate_number])

    def __str__(self):
        return self.user.__str__()

    def hours_this_week(self):
        """
        TODO: Docstring
        """
        this_users_records = StudyHoursRecord.objects.filter(user=self.user)
        return sum(
            record.number_of_hours
            for record in this_users_records
            if occurred_this_week(record.date)
        )

    def save(self, *args, **kwargs):  # pylint: disable=arguments-differ
        """
        TODO: Docstring
        """
        existing_entry = TrackedUser.objects.filter(user=self.user)

        if existing_entry.count() != 0:
            existing_entry.update(number_of_hours=self.number_of_hours)
        else:
            # Call the "real" save() method.
            super(TrackedUser, self).save(*args, **kwargs)

    class Meta:
        permissions = (("scholarship_head", "Can modify study hours."),)


class StudyHoursRecord(ModelMixin, models.Model):
    """
    Model for a record of study hours made by one tracked user for one day.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_hours = models.IntegerField(validators=[validate_number])
    date = models.DateField(validators=[validate_date])
    time_stamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return (
            "Study hours by "
            + self.user.first_name
            + " "
            + self.user.last_name
            + " on "
            + self.date.__str__()
        )

    def happened_this_week(self):
        """
        Returns whether the study hours were recorded for this week.

        Returns: bool
        """
        return occurred_this_week(self.date)


class AcademicResource(ModelMixin, models.Model):
    """
    Model for an academic resource.
    """

    resource_name = models.CharField(max_length=1000)
    course_number = models.CharField(max_length=100)
    professor_name = models.CharField(max_length=100)
    resource_pdf = models.FileField(upload_to="protected/scholarship/resources")
    submittedBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)
    year = models.IntegerField(blank=True)
    term = models.CharField(
        blank=True,
        max_length=1,
        choices=(
            ("A", "A Term"),
            ("B", "B Term"),
            ("C", "C Term"),
            ("D", "D Term"),
            ("E", "E Term"),
        ),
    )

    def __str__(self):
        return str(self.course_number) + ": " + str(self.resource_name)

    def clean(self):
        # Strip all non alpha-numeric characters from the class name
        if self.course_number:
            self.course_number = self.course_number.strip()
            self.course_number = re.sub(r"\W+", "", self.course_number)


class LibraryItem(ModelMixin, models.Model):
    """
    Model for a library item.
    """

    def __str__(self):
        return str(self.isbn_number) + ": " + str(self.title)

    def clean(self):
        """
        Standardize ISBN.
        """
        if self.isbn_number:
            self.isbn_number = self.isbn_number.strip()
            self.isbn_number = re.sub(r"\W+", "", self.isbn_number)

    title = models.CharField(max_length=1000)
    isbn_number = models.CharField(max_length=100)
    course = models.CharField(max_length=10, default="", blank=True)
    edition = models.CharField(max_length=100)
    item_pdf = models.FileField(upload_to="protected/scholarship/library")
    submittedBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)


class Course(ModelMixin, models.Model):
    """
    Holds information about a WPI Catalog Course, i.e. CS1004.
    """

    catalog_code = models.CharField(
        max_length=10, validators=[RegexValidator(regex=r"[A-Z]+[0-9]+")], unique=True
    )
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.catalog_code)


class CourseSection(ModelMixin, models.Model):
    """
    Holds info for a single instance of the course.
    """

    class Term(models.TextChoices):
        A = "A", _("A")
        B = "B", _("B")
        C = "C", _("C")
        D = "D", _("D")
        E = "E", _("E")
        S = "S", _("S")
        F = "F", _("F")

    catalog_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, to_field="catalog_code"
    )
    term = models.CharField(max_length=1, choices=Term.choices, default=Term.A)

    year = models.PositiveIntegerField(validators=[validators.MaxValueValidator(99)])
    professor = models.CharField(max_length=100)
    participants = models.ManyToManyField(User)


class Review(ModelMixin, models.Model):
    """
    Represents a single review for a course.
    """

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[validate_stars])
    text = models.CharField(max_length=1000)
