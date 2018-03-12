#!python
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

class Deck:
    '''
    DECK
    '''
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for i in range(2, 11):
                self.cards.append(Card(suit, str(i)))
            for name in NAMES:
                self.cards.append(Card(suit, name))

    def __str__(self):
        print_string = str()
        for i, card in enumerate(self.cards):
            print_string += str(i) + ": " + str(card) + "\n"
        return print_string

    def __len__(self):
        ''' Return the number of cards still in the deck '''
        return len(self.cards)

    def take_next(self):
        ''' Take a card from the "top" of the deck '''
        return self.cards.pop(0)

    def take_all(self):
        ''' Take all the cards out of the deck '''
        cards = self.cards.copy()
        self.cards.clear()
        return cards

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

