# -*- coding: utf-8 -*-
import numpy as np

class ShelvesHandler():
    def __init__(self, shelves=list()):
        self.shelves = shelves
    
    def addShelf(self, shelf):
        self.shelves.append(shelf)
    
    def sort(self, item):
        return item[1]
    
    def rankViableShelfs(self, productSize):
        difference = list()
        for shelf in self.shelves:
            if shelf.fitsInShelf(productSize):
                difference.append((shelf, shelf.calculateVolumeDifference(productSize)))
        sortedShelves = np.array(sorted(difference, key=self.sort))
        return sortedShelves[:,0]