# -*- coding: utf-8 -*-

import unittest
import numpy as np
from shelf.shelf import Shelf
from shelf.shelvesHandler import ShelvesHandler
from shelf.product import Product

class shelfTests(unittest.TestCase):
    
    def test_shelvesHandler_return_list_with_the_smallest_shelf_that_fits_first(self):
        shelfNames = ["mini", "small", "medium", "large", "gigantic"]
        shelfSizes = [(0.5, 0.5, 0.5), (1,2,2), (2,2,1), (1,3,3), (5,5,5)]
        shelfSizes = np.array(shelfSizes)
        
        shelvesHandler = ShelvesHandler()
        for i in range(len(shelfNames)):
            shelvesHandler.addShelf(Shelf(shelfNames[i], shelfSizes[i]))
        
        product = Product(np.array([2,1,1]), 10, 'Sven Svensson')
        
        self.assertEqual("medium", shelvesHandler.rankViableShelfs(product.size)[0].name)