#!python
'''
Tests for blackjack module
'''

import unittest
from blackjack import Deck, Card

class TestDeck(unittest.TestCase):

    def test_take_next(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)
        card = deck.take_next()
        self.assertEqual(len(deck), 51)
        self.assertEqual(card, Card('clubs', '2'))

    def test_take_all(self):
        deck = Deck()
        cards = deck.take_all()
        self.assertEqual(len(deck), 0)
        self.assertEqual(len(cards), 52)

if __name__ == "__main__":
    unittest.main()
