"""
Program: set_assignment
Author: Ryan Blankenship
Last date modified: 10/12/2019

The purpose of this program is to return True
if a value is in a set or False if it is not.
"""


def in_set(this_set, a_value):
    """
    function to check if a value is in a set
    :param this_set: set of numbers
    :param a_value: value to check if in set
    :return: True if value found or False if not
    """
    if a_value in this_set:
        return True
    else:
        return False


if __name__ == '__main__':
    in_set()
