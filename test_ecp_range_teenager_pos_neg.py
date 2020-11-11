import unittest
from is_teenager import is_Teenager

class TeenTestCase(unittest.TestCase):

    def test_pos(self):
        a = 14
        if a >= 13 and a < 20:
            self.assertTrue(is_Teenager(a))

    
    def test_neg(self):
        wrong = [0, None, "", " ", [], 12, 20, 16.7, -10]
        for a in wrong:
            if a in wrong:
                self.assertFalse(is_Teenager(a))



if __name__ == '__main__':
    unittest.main()
