# -*- coding: utf-8 -*-
from shelf.product import Product
from shelf.shelf import Shelf
from shelf.shelvesHandler import ShelvesHandler

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

shelvesHandler = ShelvesHandler()
for i in range(len(shelfNames)):
    shelvesHandler.addShelf(Shelf(shelfNames[i], shelfSizes[i]))

product = Product(np.array([2,1,1]), 10, 'Sven Svensson')

print("The best fit shelf is: {}".format(shelvesHandler.rankViableShelfs(product.size)[0].name))