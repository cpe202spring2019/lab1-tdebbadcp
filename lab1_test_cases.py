import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Testing for ValueError if None is passed."""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        """Testing for None if empty list is passed."""
        self.assertEqual(max_list_iter([]) , None)
        """If max is right most."""
        self.assertEqual(max_list_iter([12, 2 ,2 , 23 , 7 , 25]) ,25)
        """If max is left most."""
        self.assertEqual(max_list_iter([27, 2 ,2 , 23 , 7 , 19]) ,27)
        """If max is in the middle."""
        self.assertEqual(max_list_iter([1, 2 ,2 , 29 , 7 , 19]) ,29)
        """If list contains elements of the same value."""
        self.assertEqual(max_list_iter([7,7,7,7,7]) ,7)
        """If max value is the first and last element."""
        self.assertEqual(max_list_iter([7, 5, 2, 7]) ,7)
        """If max value is repeated in the beginning."""
        self.assertEqual(max_list_iter([7 , 7 , 2, 1 , 6]) ,7)
        """If max value is repeated in the end."""
        self.assertEqual(max_list_iter([2 , 1 , 2, 1 , 7 , 7]) ,7)

    def test_reverse_rec(self):
        """If None is passes ValueError is raised."""
        self.assertEqual(reverse_rec([1,2,3]), [3,2,1])
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
        """If empty list is passed empty list is returned."""
        self.assertEqual(reverse_rec([]) , [])
        """If list has one element"""
        self.assertEqual(reverse_rec([3]) , [3])
        """Reverses list with different elements."""
        self.assertEqual(reverse_rec([1,2,3,4]) ,[4,3,2,1])
        """Reverses list with repeating elements."""
        self.assertEqual(reverse_rec([1,1,2,1,2,1]) ,[1,2,1,2,1,1])
        """Reverses list having all the same elements."""
        self.assertEqual(reverse_rec([1,1,1,1]), [1,1,1,1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        """If target is in the middle."""
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        """If target is not in list and is greater than values in the list."""
        self.assertEqual(bin_search(23, 0, len(list_val)-1, list_val), None)
        """If target is not in list and is less than values in the list."""
        self.assertEqual(bin_search(-10, 0, len(list_val)-1, list_val), None)
        """If list passed is None."""
        list_val = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(4, 0, 5, list_val)
        """If target is the first element of list."""
        list_val =[0,1,2,3,4]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)
        """If target is the last element of list."""
        list_val =[1,2,3,4,5]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), 4)
        """If list has repeating elements and target is first element."""
        list_val =[1,2,2,3,4]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 0)
        """If list has repeating elements and target is last element."""
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        """If list has all the same elements."""
        list_val =[2,2,2,2,2]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), 2)
        """If list contains negative numbers."""
        list_val =[-1,-1,0,3,5,6,7]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3)

if __name__ == "__main__":
        unittest.main()

    
