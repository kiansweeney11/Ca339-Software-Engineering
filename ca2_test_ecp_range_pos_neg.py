import unittest

from is_day_in_regular_year import is_day_in_reg_year

class DayTestCase(unittest.TestCase):

    def test_pos(self):
        a = 1
        if a >= 1 and a <= 365:
            self.assertTrue(is_day_in_reg_year(a))

    def test_neg(self):
        wrong = ["", " ", 0, 366, -1, 16.5, [], None]
        for a in wrong:
            if a in wrong:
                self.assertFalse(is_day_in_reg_year(a))




if __name__ == '__main__':
    unittest.main()
