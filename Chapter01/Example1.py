'''
Created on May 16, 2019

@author: Karteek
'''

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    rank = [str(n) for n in range(2,11)] + list('JQKA')
    suit = 'spades daimonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suit for rank in self.rank]
        
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
