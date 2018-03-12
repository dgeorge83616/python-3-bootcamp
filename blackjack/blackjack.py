#!python

import random

'''
BLACKJACK GAME
'''
SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
NAMES = ['Jack', 'Queen', 'King', 'Ace']

class Card:
    '''
    SIMPLE STRUCTURE FOR A CARD
    '''
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def __str__(self):
        return f"{self.suit}, {self.name}"

    def __eq__(self, value):
        return self.suit == value.suit and self.name == value.name

    def get_name(self):
        ''' Return just the name of this card '''
        return self.name

    def get_suit(self):
        ''' Return just the suit of this card '''
        return self.suit

MARKER = Card("MARKER", "MARKER")

class Deck(list):
    '''
    DECK
    '''
    def __init__(self):
        pass

    def fill_deck():
        ''' Put cards into the deck '''
        for suit in SUITS:
            for i in range(2, 11):
                self.append(Card(suit, str(i)))
            for name in NAMES:
                self.append(Card(suit, name))

    def take_next(self):
        ''' Take a card from the "top" of the deck '''
        return self.pop(0)

    def take_all(self):
        ''' Take all the cards out of the deck '''
        cards = self.copy()
        self.clear()
        return cards

    def shuffle(self):


class Pack(Deck):
    ''' Holds the decks that will be used for the table '''

    def __init__(self, decks):
        for deck in decks:
            self.cards += deck.take_all()

    def __len__(self):
        '''
        Return the number of cards still in the pack
        '''
        return len(self.cards)

    def insert_marker(self, position):
        ''' As named '''
        self.cards.insert(position, MARKER)

class Hand:
    pass

class Player:
    pass

class Dealer:
    pass


if __name__ == "__main__":
    DECK = Deck()
    print(f"{DECK}")
    CARD = Card('clubs', '2')
    card = DECK.take_next()
    print(f"{card}")
    if card == CARD:
        print("equal")
    else:
        print("not equal")
    print(f"{DECK}")

