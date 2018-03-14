#!python
'''
Tests for blackjack module
'''

import unittest
from prog import Pack
from prog import Game
from prog import Player

class InputMock:
    ''' mock prompter '''
    def __init__(self, inputs):
        self.inputs = inputs

    def noop(self):
        ''' defeat pylint too-few-public methods '''
        self.inputs = self.inputs

    def prompt(self, prompt_str):
        ''' just returns the next test response '''
        # defeat pylint
        prompt_str = prompt_str
        return self.inputs.pop(0)

class TestRegistration(unittest.TestCase):
    ''' Class for testing registration '''

    def test_registration(self):
        ''' simple test for registration '''
        print(f"{self.test_registration}")
        players = [Player('Dan', 200, [])]
        inputs = ['y', players[0].name, str(players[0].balance), 'n']
        new_players = Game.get_new_players(InputMock(inputs))
        self.assertEqual(players, new_players)


class TestPlayer(unittest.TestCase):
    ''' Class for testing Player '''

    def test_init(self):
        ''' Test the __init__ method '''
        print(f"{self.test_init}")
        player = Player('Jose', 500, InputMock([]))
        print(f"Initialized player: {player}")

    def test_bet(self):
        ''' Test making a bet '''
        print(f"{self.test_bet}")
        prompter = InputMock([10, 100, 101, 50, 9, 11, 'p'])
        player = Player('Jose', 500, prompter)
        wager_limits = (10, 100)
        player.bet(wager_limits)
        self.assertEqual(player.wager, 10)
        player.bet(wager_limits)
        self.assertEqual(player.wager, 100)
        player.bet(wager_limits)
        self.assertEqual(player.wager, 50)
        player.bet(wager_limits)
        self.assertEqual(player.wager, 11)
        self.assertFalse(player.bet(wager_limits))

    def test_play(self):
        ''' Test playing '''
        print(f"{self.test_play}")
        prompter = InputMock(['y',])
        player = Player('Jose', 500, prompter)
        player.hand += ['10', '4']
        cards = ['10']
        player.play(cards)
        self.assertTrue(player.hand)
        self.assertTrue(player.hand.val() > 21)

class TestPack(unittest.TestCase):
    ''' Tests for Pack '''

    def test_init(self):
        ''' Test the __init__ method '''
        print(f"{self.test_init}")
        pack = Pack(1)
        #print(pack)
        self.assertEqual(len(pack), 52)
        pack = Pack(4)
        #print(pack)
        self.assertEqual(len(pack), 4*52)

class TestBlackjack(unittest.TestCase):
    ''' Tests for the game '''

    def test_play_game(self):
        ''' Example game session '''
        print(f"{self.test_play_game}")
        max_draws = ['y']*10
        player_inputs = [10] + max_draws
        game = Game(Player('Dealer', 0, InputMock(max_draws.copy())),\
                Pack(1), (10, 100),\
                [Player('Dan', 100, InputMock(player_inputs.copy())),\
                Player('Gayle', 500, InputMock(player_inputs.copy())),\
                Player('Jose', 350, InputMock(player_inputs.copy()))])
        game.play()
        game.settle_bets()
        print(f"pushes: {game.pushes}")
        print(f"busts: {game.inactive_players}")

if __name__ == "__main__":
    unittest.main()
