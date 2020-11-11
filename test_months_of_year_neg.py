import unittest
from is_month_of_year import is_Month_Of_Year


class MonthTestCase(unittest.TestCase):

    def test_month(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        for string in months:
            if string not in months:
                self.assertFalse(is_Month_Of_Year(string))


if __name__ == '__main__':
    unittest.main()
