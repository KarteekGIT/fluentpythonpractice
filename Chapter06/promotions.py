'''
Created on May 27, 2019

@author: AA
'''

def fidelity_promo(order):
        return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0
    
def bulk_item_promo(order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount
    
def large_order_promo(order):
        distinct_items = {items.product for items in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.7
        return 0