import unittest

from is_day_in_the_week import is_Day_In_The_Week

class DayTestCase(unittest.TestCase):

    def test_pos(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        wrong= ["", " ", 0, 16.2, None]
        for a in wrong:
            if a in wrong and a not in days:
                self.assertFalse(is_Day_In_The_Week(a))




if __name__ == '__main__':
    unittest.main()
