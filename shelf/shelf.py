# -*- coding: utf-8 -*-
 
import pandas as pd
import numpy as np
import random

class Shelf():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
    def fitsInShelf(self, productSize):
        return all([(productSize <= shelfSize) 
                    for productSize,shelfSize in zip(productSize, self.size)])
    
    def calculateVolumeDifference(self, productSize):
        return(np.prod(self.size) - np.prod(productSize))

        
