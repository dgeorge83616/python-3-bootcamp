#!python
'''
Tests for blackjack module
'''

import unittest
from blackjack import Pack, Game, Player

class TestPlayer(unittest.TestCase):

    class InputMock:
        ''' mock prompter '''
        def __init__(self, inputs):
            self.inputs = inputs

        def prompt(self, name):
            ''' just returns the next test response '''
            return self.inputs.pop(0)

    def test_init(self):
        print(f"{self.test_init}")
        player = Player('Jose', 500, TestPlayer.InputMock(list([])))
        print(f"Initialized player: {player}")

    def test_bet(self):
        print(f"{self.test_bet}")
        prompter = TestPlayer.InputMock([10, 100, 101, 50, 9, 11, 'p'])
        player = Player('Jose', 500, prompter)
        player.bet(10, 100)
        self.assertEqual(player.wager, 10)
        player.bet(10, 100)
        self.assertEqual(player.wager, 100)
        player.bet(10, 100)
        self.assertEqual(player.wager, 50)
        player.bet(10, 100)
        self.assertEqual(player.wager, 11)
        self.assertFalse(player.bet(10, 100))

    def test_play(self):
        print(f"{self.test_play}")
        prompter = TestPlayer.InputMock(['y', 'y', 'y'])
        player = Player('Jose', 500, prompter)
        cards = ['10', '10', '10']
        player.play(cards)
        print(f"Hand = {player.hand}")
        self.assertTrue(player.hand)
        self.assertTrue(player.hand.val() > 21)

class TestPack(unittest.TestCase):

    def test_init(self):
        print(f"{self.test_init}")
        pack = Pack(1)
        #print(pack)
        self.assertEqual(len(pack), 52)
        pack = Pack(4)
        #print(pack)
        self.assertEqual(len(pack), 4*52)

class TestBlackjack(unittest.TestCase):

    def test_play_game(self):
        print(f"{self.test_play_game}")
        max_draws = ['y']*10
        player_inputs = [10] + max_draws
        game = Game(Player('Dealer', 0, TestPlayer.InputMock(max_draws.copy())),\
                Pack(1), (10, 100),\
                [Player('Dan', 100, TestPlayer.InputMock(player_inputs.copy())),\
                Player('Gayle', 500, TestPlayer.InputMock(player_inputs.copy())),\
                Player('Jose', 350, TestPlayer.InputMock(player_inputs.copy()))])
        game.play()
        if game.winners:
            print("Winners:")
            for winner in game.winners:
                print(f"       {winner.name}, {winner.hand}")
        print(f"pushes: {game.pushes}")
        print(f"busts: {game.inactive_players}")

if __name__ == "__main__":
    unittest.main()
