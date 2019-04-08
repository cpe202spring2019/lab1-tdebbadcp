import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq(self):
        loc1 = Location("Paris", 48.9, 2.4)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = 'String'

        self.assertEqual(loc1 == loc2, False)
        self.assertEqual(loc2 == loc3, True)
        self.assertEqual(loc1 == loc4, False)


if __name__ == "__main__":
        unittest.main()
