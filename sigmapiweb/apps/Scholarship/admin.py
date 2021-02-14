"""
Admin config for Scholarship app.
"""
from common.utils import register_model_admins

from .models import (
    AcademicResource,
    LibraryItem,
    StudyHoursRecord,
    TrackedUser,
    Course,
    CourseSection,
    Review,
)


register_model_admins(
    AcademicResource,
    LibraryItem,
    StudyHoursRecord,
    TrackedUser,
    Course,
    CourseSection,
    Review,
)
