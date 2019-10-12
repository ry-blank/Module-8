import unittest
from more_fun_with_collections import dict_membership


class DictTest(unittest.TestCase):
    def test_in_dict_true(self):
        dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        expected_result = True
        self.assertEqual(expected_result, dict_membership.in_dict(dict, 'E'), True)

    def test_in_dict_false(self):
        dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        expected_result = False
        self.assertEqual(expected_result, dict_membership.in_dict(dict, 'F'), False)


if __name__ == '__main__':
    unittest.main()
