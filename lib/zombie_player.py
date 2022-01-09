#! /usr/lib/python3

# .lib/zombie_player.py

import game_dice


class ZombiePlayer():
    'handles player info'
    def __init__(self, name = input('Enter zombie name: \n')):
        self.name = name
        self.brains = 0
        self.shotguns = 0
        self.dice = [0, 0, 0]

    def display_dice(self):
        'display the players current dice'
        print('Dice in inventory:')
        print(f'Green dice: {self.dice[0]}')
        print(f'Yellow dice: {self.dice[1]}')
        print(f'Red dice: {self.dice[2]}')

    def update_scores(self, dice_roll):
        'takes a dice roll and updates the players values'
        self.dice = [0, 0, 0]
        self.brains = dice_roll['b']
        self.shotguns = dice_roll['s']
        for _ in range(dice_roll['f']['g']):
            self.dice[0] += 1
        for _ in range(dice_roll['f']['y']):
            self.dice[1] += 1
        for _ in range(dice_roll['f']['r']):
            self.dice[2] += 1

    def display_score(self):
        'show current score'
        print(f'Brains: {self.brains}')
        print(f'Shotguns: {self.shotguns}')
