'''
Created on May 16, 2019

@author: AA
'''
from Chapter01.Example1 import Card, FrenchDeck
def execEx1():
    
    beer_card = Card('7','daimonds')
    print(beer_card)
    
    deck = FrenchDeck()
    print(len(deck))
    
    for i in range(0,len(deck)):
        print(deck[i])
        
    from random import choice
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    
    print(deck[:3])
    print(deck[12::13])
    
    for card in deck:
        print(card)
        
    for card in reversed(deck):
        print(card)
        
        
    suit_values = dict(spades=3, hearts=2, daimonds=1, clubs=0)
    
    def spades_high(card):
        rank_value = FrenchDeck.rank.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
        
    for card in sorted(deck, key = spades_high):
        print(card)
        
if __name__ == '__main__':execEx1()