import unittest
from is_prime import is_Prime

class PrimesTestCase(unittest.TestCase):

    def test_neg(self):
        self.assertFalse(is_Prime(6))

    def test_pos(self):
        self.assertTrue(is_Prime(5))
       
                   
if __name__ == '__main__':
    unittest.main()
