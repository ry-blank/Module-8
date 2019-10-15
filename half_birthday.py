"""
Program: python_datetime_assignment
Author: Ryan Blankenship
Last date modified: 10/14/2019

The purpose of this program is to use
Python datetime to calculate the date
the half birthday falls on.
"""
from datetime import date, timedelta


def half_birthday(b_day):
    """
    function for half birthday
    :param b_day: most recent birthday
    :return: half birthday
    """
    half_b_day = b_day + timedelta(days=182.5)
    return half_b_day
