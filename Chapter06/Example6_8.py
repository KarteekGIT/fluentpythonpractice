'''
Created on May 27, 2019

@author: AA
'''
import inspect
from Chapter06 import promotions
from inspect import isfunction
'''
Created on May 27, 2019

@author: AA
'''
from collections import namedtuple
from ctypes.test.test_pickling import name

Customer = namedtuple('customer', 'name fidelity')

class LineItem:
    def __init__(self, product,quantity,price):
        self.product = product
        self.quantity = quantity
        self.price = price
        
    def total(self):
        return self.quantity * self.price
    
class Order: #The content
    def __init__(self,customer,cart,promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
        
    def total(self):
        if not hasattr(self, '_total'):
            self._total = sum(items.total() for items in self.cart)
        return self._total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order Total : {:.2f}   due : {:.2f}'
        return fmt.format(self.total(), self.due())

promo_List = [func for name, func in inspect.getmembers(promotions, isfunction)]

def best_promo(order):
    return max(promo(order) for promo in promo_List)
    
if __name__ == '__main__':
    joe = Customer('Jhon doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, 0.5), LineItem('apple', 10, 1.5), LineItem('Watermellon', 5, 5.0)]
    print(Order(joe, cart, best_promo))
    print(Order(ann,cart,best_promo))
    banana_cart = [LineItem('banana', 30, 0.5), LineItem('apple',10,1.5)]
    print(Order(joe,banana_cart,best_promo))
    long_order = [LineItem(str(item_code),1,1.0) for item_code in range(10)]
    print(Order(joe,long_order,best_promo))
    print(Order(joe,cart,best_promo))
    #print(globals())