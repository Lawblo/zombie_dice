#! /usr/lib/python3

# .lib/new_game.py

import zombie_player

class NewGame():
    def __init__(self, player1 = input('Player 1:\n'), player2 = input('Player 2:\n')):
        self.player1 = zombie_player.ZombiePlayer(player1)
        self.player2 = zombie_player.ZombiePlayer(player2)
        self.welcome()

    def welcome(self):
        print(f'Welcome {self.player1.name} and {self.player2.name}')
