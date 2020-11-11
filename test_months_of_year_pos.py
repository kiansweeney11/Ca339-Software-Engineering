import unittest
from is_month_of_year import is_Month_Of_Year

class MonthTestCase(unittest.TestCase):

    def test_pos(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        for a in months:
            if a in months:
                self.assertTrue(is_Month_Of_Year(a))


if __name__ == '__main__':
    unittest.main()
