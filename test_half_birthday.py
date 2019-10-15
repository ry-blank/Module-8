import unittest
from more_fun_with_collections import half_birthday


class HalfBirthday(unittest.TestCase):
    def test_half_birthday(self):
        most_recent_birthday = half_birthday.date(2019, 7, 21)
        my_half_birthday = half_birthday.date(2020, 1, 19)
        self.assertEqual(half_birthday.half_birthday(most_recent_birthday), my_half_birthday)


if __name__ == '__main__':
    unittest.main()
