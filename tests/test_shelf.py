# -*- coding: utf-8 -*-

import unittest
import numpy as np
from shelf.shelf import Shelf

class shelfTests(unittest.TestCase):
    
    def test_shelf_should_fit_in_shelf_if_all_dimensions_are_smaller_or_equal_to_shelf(self):
        shelf = Shelf("small",  np.array([2,2,2]))
        self.assertTrue(shelf.fitsInShelf(np.array([1,2,1])))
        
    def test_shelf_should_not_fit_in_shelf_if_one_dimension_is_larger_than_shelf(self):
        shelf = Shelf("small",  np.array([2,2,2]))
        self.assertFalse(shelf.fitsInShelf(np.array([1,3,1])))
        
    def test_shelf_calculateVolumeDifference_return_correct_result(self):
        shelf = Shelf("small",  np.array([2,2,2]))
        self.assertEqual(6, shelf.calculateVolumeDifference(np.array([1,2,1])))