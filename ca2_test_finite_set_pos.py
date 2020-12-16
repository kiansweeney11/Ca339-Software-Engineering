import unittest

from is_colour_of_the_rainbow import is_Colour_Of_The_Rainbow

class RainbowTestCase(unittest.TestCase):

    def test_pos(self):
        colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        for a in colours:
            if a in colours:
                self.assertTrue(is_Colour_Of_The_Rainbow(a))




if __name__ == '__main__':
    unittest.main()
