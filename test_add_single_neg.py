import unittest
from add import add

class AddTestCase(unittest.TestCase):

    def test_add(self):
        self.assertNotEqual(add(2,2), 5)

    
if __name__ == '__main__':
    unittest.main()
