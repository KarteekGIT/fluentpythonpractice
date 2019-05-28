'''
Created on May 27, 2019

@author: AA

Decorator enhanced strategy pattern
'''
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
            discount = self.promotion(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order Total : {:.2f}   due : {:.2f}'
        return fmt.format(self.total(), self.due())

promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order): #First functional strategy
        return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0
    
@promotion    
def bulk_item(order): #Second functional strategy
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount

@promotion    
def large_order(order): #Third functional strategy
        distinct_items = {items.product for items in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.7
        return 0
    
def best_promo(order):
    return max(promo(order) for promo in promos)

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