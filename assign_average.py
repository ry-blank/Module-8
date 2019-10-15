"""
Program: selection_using_dictionary_assignment
Author: Ryan Blankenship
Last date modified: 10/14/2019

The purpose of this program is to use a
dictionary to mimic a switch statement
to return the value of a key.
"""


def switch_average(key):
    """
    function to use dict to mimic switch
    :param key: key of value to be found
    :return: value of key or KeyError message
    """
    return {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4
    }.get(key, KeyError)
