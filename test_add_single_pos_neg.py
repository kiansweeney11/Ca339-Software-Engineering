import unittest
from add import add

class AddTestCase(unittest.TestCase):

    def test_pos(self):
        self.assertEqual(add(2,2), 4)

    def test_neg(self):
        self.assertNotEqual(add(3,3), 7)
        

    
if __name__ == '__main__':
    unittest.main()
