''' Classes'''

class  StockItem(object):
    def __init__(self, uniqueID, clientName, pricePerUnit, warehouseNumber):
    
        self.uniqueID = uniqueID
        self.clientName = clientName
        self.pricePerUnit = pricePerUnit
        self.warehouseNumber = warehouseNumber
        
        ''' The str method prints an instance of a stock item'''
        
    def __str__(self):
        return  '%d, %s, %f, %d' %(self.uniqueID, self.clientName, self.pricePerUnit, self.warehouseNumber)


    def __add__(self, pricePerUnit):
        ''' Perform addition with parameter 3'''
        print 'in add' # trace print
        sum = self.value + pricePerUnit.value
        return StockItem(sum)
        
        Stock1.__add__(Stock2)
        
Stock1 = StockItem(702, 'Moore', 74, 879956)  
print Stock1
      
      
Stock2 = StockItem(668, 'OConnellMeats', .968, 462278) 
print Stock2