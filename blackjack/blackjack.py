#!python
'''
BLACKJACK GAME
'''
from random import shuffle

SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
FACE_CARDS = ['J', 'Q', 'K']
NUMS = ['2', '3', '4', '5', '6', '7', '8', '9', '10']

class Prompter:
    ''' As named '''
    def __init__(self):
        pass

    def prompt(self, prompt):
        ''' simple promt using stdin '''
        return input(prompt)

class Pack(list):
    ''' Pack of cards '''
    def __init__(self, num_decks):
        full_suit = NUMS + FACE_CARDS + ['A']
        full_deck = full_suit*len(SUITS)
        super().__init__(full_deck*num_decks)

def card_value(card):
    ''' As named '''
    if card in FACE_CARDS:
        return 10
    if card == 'A':
        return 11
    return int(card)

class Hand(list):
    ''' As named '''

    def val(self):
        ''' Return the sum of the cards '''
        val = 0
        for card in self:
            val += card_value(card)
            if val > 21 and 'A' in self:
                self[self.index('A')] = '1'
                val -= 10
        return val

class Player:
    ''' Represents a player in the game '''

    def __init__(self, name, balance, prompter):
        self.name = name
        self.balance = balance
        self.prompter = prompter
        self.wager = 0
        self.hand = Hand()

    def __str__(self):
        return f"{self.name}, {self.balance}, {self.wager}, {self.hand}"

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def bet(self, min_wager, max_wager):
        ''' As named, return True if made a bet. '''
        if self.balance < min_wager:
            return False
        max_wager = min(self.balance, max_wager)
        while True:
            wager = str(self.prompter.prompt(f"{self.name}, make bet: "))
            if wager.lower() == 'p':
                return False
            if wager.lower() == '$':
                print(f"Bank balance: ${self.balance}")
                continue
            wager = int(wager)
            if min_wager <= wager and wager <=  max_wager:
                break
        self.wager = wager
        self.balance -= self.wager
        return True

    def hit(self, card):
        self.hand += [str(card)];
        return self.hand.val()

    def play(self, cards):
        ''' play till stand or busted '''
        while True:
            answer = str(self.prompter.prompt(f"{self.name}, take a card? (y/n): "))
            if answer.lower() != 'y':
                break
            elif self.hit(cards.pop()) > 21:
                break

class Game:
    ''' As named '''

    def __init__(self, dealer, pack, wager_limits, players):
        self.dealer = dealer
        self.pack = pack
        self.min_bet = wager_limits[0]
        self.max_bet = wager_limits[1]
        self.players = players
        self.winners = []
        self.inactive_players = []
        self.pushes = []

    def remove_inactive_players(self):
        for player in self.inactive_players:
            if player in self.players:
                self.players.remove(player)

    def take_bets(self):
        ''' As named and remove non-betters '''
        # take bets
        for player in self.players:
            if not player.bet(self.min_bet, self.max_bet):
                self.inactive_players.append(player)
        # remove non-bettors
        self.remove_inactive_players()

    def deal_cards(self):
        ''' As named and return winners list, which may be empty '''
        for player in self.players:
            player.hit(self.pack.pop())
        self.dealer.hit(self.pack.pop())
        for player in self.players:
            hand = player.hit(self.pack.pop())
            if hand > 21:
                self.inactive_players.append(player)
            elif hand == 21:
                # Game over - player wins
                self.winners = [player]
                break
        # remove busted players
        self.remove_inactive_players()

        if self.winners:
            return bool(self.winners)

        hand = self.dealer.hit(self.pack.pop())
        if hand > 21:
            # Game over players win
            self.winners = self.players
        elif hand == 21:
            # Game over
            self.winners.append(self.dealer)
        return bool(self.winners)

    def payout(self):
        pass

    def play(self):
        ''' main processing loop '''
        shuffle(self.pack)

        self.take_bets()
        if not self.players:
            return

        if self.deal_cards():
            return
        print(f"Players:")
        for player in self.players:
            print(f"         {player}")
        if int(card_value(self.dealer.hand[1])) >= 10:
            dealer_shows = self.dealer.hand
        else:
            dealer_shows = ['X', self.dealer.hand[1]]
        print(f"Dealer: {dealer_shows}")

        for player in self.players:
            player.play(self.pack)
            if player.hand.val() > 21:
                self.inactive_players.append(player)
            else:
                max_hand = max(max_hand, player.hand.val())
        self.remove_inactive_players()

        while self.dealer.hand.val() < 17:
            self.dealer.hit(self.pack.pop())
        if self.dealer.hand.val() > 21:
            self.winners = self.players
            return

        for player in self.players:
            if player.hand.val() >  self.dealer.hand.val():
                self.winners.append(player)
            if player.hand.val() == self.dealer.hand.val():
                self.pushes.append(player)

        self.payout()

if __name__ == "__main__":
    pass
