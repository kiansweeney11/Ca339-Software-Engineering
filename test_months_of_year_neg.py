import unittest
from is_month_of_year import is_Month_Of_Year


class MonthTestCase(unittest.TestCase):

    def test_month(self):
        fails = ["", " ", None, 0, {}, 16.2]
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        for a in fails:
            if a in fails and a not in months:
                self.assertFalse(is_Month_Of_Year(a))


if __name__ == '__main__':
    unittest.main()
