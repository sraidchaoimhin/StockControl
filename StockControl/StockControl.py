

import datetime

''' Classes'''

class  StockItem(object):
    def __init__(self, uniqueID, clientName, pricePerUnit, warehouseNumber):
    
        self.uniqueID = uniqueID
        self.__clientName = clientName
        self.pricePerUnit = pricePerUnit
        self.warehouseNumber = warehouseNumber
        
        ''' The str method prints an instance of a stock item'''
        
    def __str__(self):
        return  '%d, %s, %f, %d' %(self.uniqueID, self.clientName, self.pricePerUnit, self.warehouseNumber)


    def __add__(self, secondItem):
        ''' Perform addition using parameter 3'''
        sum = self.pricePerUnit + secondItem.pricePerUnit
        return sum
        
    def __mul__(self, x):
        ''' Perform multiplication using parameter 3'''
        sum = self.pricePerUnit * x
        return sum
    
    def CalculateStorageCost(self):
        ''' Multiplacation by .05 to get Storage Cost'''
        sum = self.pricePerUnit * .05
        return sum
    
class  CD(StockItem):
    def __init__(self, title, dateReleased, genre, artist, uniqueID, clientName, pricePerUnit, warehouseNumber):
        StockItem.__init__(self, uniqueID, clientName, pricePerUnit, warehouseNumber)
    
        self.title = title
        self.dateReleased = dateReleased
        self.genre = genre
        self.artist = artist
        
    def __str__(self):
        return  '%s, %d, %s, %s, %d, %f, %d' %(self.title, self.dateReleased, self.genre, self.artist, self.uniqueID, self.pricePerUnit, self.warehouseNumber)
        

    def GetDateReleased(self):
        return '%s' %(self.dateReleased)

    def IsAPreRelease(self):
        return '%b' %(dateReleased)

    def DiscountMultipleCdPurchase(self, x):
        sum = self.pricePerUnit * x * .9
        return sum

        
class  Book(StockItem):
    def __init__(self, title, dateReleased, genre, author, uniqueID, clientName, pricePerUnit, warehouseNumber):
        StockItem.__init__(self, uniqueID, clientName, pricePerUnit, warehouseNumber)

        self.title = title
        self.dateReleased = dateReleased
        self.genre = genre
        self.author = author

    def __str__(self):
        return  '%s, %d, %s, %s, %d, %s, %f, %d' %(self.title, self.dateReleased, self.genre, self.author, self.uniqueID, self.clientName, self.pricePerUnit, self.warehouseNumber)        
                
        
        
class  StockRepository(StockItem):
    def __init__(self, stockCollection, uniqueID, clientName, pricePerUnit, warehouseNumber):
        StockItem.__init__(self, uniqueID, clientName, pricePerUnit, warehouseNumber)

        self.stockCollection = stockCollection
        
class  StockException(StockItem):
    def __init__(self, className, methodName, dateOfOccurence, errorMessage, uniqueID, clientName, pricePerUnit, warehouseNumber):
        StockItem.__init__(self, uniqueID, clientName, pricePerUnit, warehouseNumber)

        self.className = className
        self.methodName = methodName
        self.dateOfOccurence = dateOfOccurence
        self.errorMessage
        
        
class  Test(object):
    def __init__(self, createItem, calculateHoldingCost, addToRepository, positionItem, deleteItem, useCode):

        self.createItem = createItem
        self.calculateHoldingCost = calculateHoldingCost
        self.addToRepository = addToRepository
        self.errorMessage = errorMessage
        self.useCode = useCode
        
        
   
    
        
Stock1 = StockItem(702, 'Moore', 74, 879956)  
print Stock1
      
      
Stock2 = StockItem(668, 'OConnellMeats', .968, 462278) 
print Stock2