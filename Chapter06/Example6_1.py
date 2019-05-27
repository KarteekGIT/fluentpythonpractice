'''
Created on May 27, 2019

@author: AA
'''
from abc import ABC, abstractmethod
from collections import namedtuple

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
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order Total : {:.2f}   due : {:.2f}'
        return fmt.format(self.total(), self.due())

class Promotion(ABC): #The Strategy: An Abstract Base Class
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""
        
class FidelityPromotion(Promotion): #First concrete strategy
    """5% discount for customers with 1000 or more fidelity points"""
    
    def discount(self, order):
        return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0
    
class BulkItemPromotion(Promotion): #Second concrete class 
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount
    
class LargeOrderPromo(Promotion): #Third concrete class 
    """7% discount for orders with 10 or more distinct items"""
    
    def discount(self, order):
        distinct_items = {items.product for items in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.7
        return 0
    
        
if __name__ == '__main__':
    joe = Customer('Jhon doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, 0.5), LineItem('apple', 10, 1.5), LineItem('Watermellon', 5, 5.0)]
    print(Order(joe, cart, FidelityPromotion()))
    print(Order(ann,cart,FidelityPromotion()))
    banana_cart = [LineItem('banana', 30, 0.5), LineItem('apple',10,1.5)]
    print(Order(joe,banana_cart,BulkItemPromotion()))
    long_order = [LineItem(str(item_code),1,1.0) for item_code in range(10)]
    print(Order(joe,long_order,LargeOrderPromo()))
    print(Order(joe,cart,LargeOrderPromo()))

