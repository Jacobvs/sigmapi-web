import datetime
from enum import Enum

class Term(Enum):
    a  = "A Term"
    b  = "B Term"
    c  = "C Term"
    d  = "D Term"
    e1 = "E1 Term"
    e2 = "E2 Term"

    @classmethod
    def choices(cls):
        return tuple((choice.name, choice.value) for choice in cls)


def allowed_years():
    """
    Generates a list of tuples of years allowed when chosing when a term for a class
    """
    current_year = datetime.date.today().year
    return [(year, year) for year in range(current_year-6, current_year)]
