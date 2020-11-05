import unittest
from add import add

class AddTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,2), 4, "There is a problem with the test, result does not match expected result")

    
if __name__ == '__main__':
    unittest.main()
