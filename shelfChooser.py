# -*- coding: utf-8 -*-
 
import pandas as pd
import numpy as np
import random

class Shelf():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        
class Product():
    def __init__(self, size, weight, owner):
        self.size = size
        self.weight = weight
        self.owner = owner

def fitsInShelf(productSize, shelfSize):
    return all([(productSize <= shelfSize) for productSize,shelfSize in zip(productSize, shelfSize)])

def calculateVolumeDifference(productSize, shelfSize):
    return(np.prod(shelfSize) - np.prod(productSize))

def sort(item):
    return item[1]

def rankViableShelfs(productSize, shelves):
    difference = list()
    for shelf in shelves:
        if fitsInShelf(productSize, shelf.size):
            difference.append((shelf, calculateVolumeDifference(productSize, shelf.size)))
    sortedShelves = np.array(sorted(difference, key=sort))
    return sortedShelves[:,0]
            
        
        
        

allowedDim = dict({'minSize':0, 'maxSize':10})

#dimensions = np.random.randint(allowedDim.get('minSize'), allowedDim.get('maxSize'), (10,3))
#maxWeights = np.empty(10)
#maxWeights[:] = np.NAN

storedata = [((1,1,1), 'None', 'Empty'),
             ((1,2,2), 'None', 'Empty'),
             ((2,2,1), 'None', 'Empty'),
             ((1,3,3), 'None', 'Empty'),
             ((5,5,5), 'None', 'Empty')]

columns = ['dimensions', 'maxWeight', 'status']

store = pd.DataFrame.from_records(storedata, columns=columns)

shelfNames = ["mini", "small", "medium", "large", "gigantic"]
shelfSizes = [(0.5, 0.5, 0.5), (1,2,2), (2,2,1), (1,3,3), (5,5,5)]
shelfSizes = np.array(shelfSizes)

shelves = list()
for i in range(len(shelfNames)):
    shelves.append(Shelf(shelfNames[i], shelfSizes[i]))

product = Product(np.array([1,1,1]), 10, 'Sven Svensson')

print("The best fit shelf is: {}".format(rankViableShelfs(product.size, shelves)[0].name))
