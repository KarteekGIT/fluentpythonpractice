'''
Created on May 26, 2019

@author: AA
'''
import random

class BingoCage:
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)
        
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty bingo cage')
        
    def __call__(self):
        return self.pick()
            
            

    