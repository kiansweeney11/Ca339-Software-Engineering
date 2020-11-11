import unittest
from is_teenager import is_Teenager

class TeenTestCase(unittest.TestCase):

    def test_pos(self):
        ages = [13,14,15,16,17,18,19]
        for a in ages:
            if a in ages:
                self.assertTrue(is_Teenager(a))

    def test_neg(self):
        incorrect = ["abc", "", 12, 20, 16.2, -3, [], None,0]
        for a in incorrect:
            self.assertFalse(is_Teenager(a))

if __name__ == '__main__':
    unittest.main()

