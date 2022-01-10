#! /usr/lib/python3
'contains info about the zombie'

# .lib/zombie_player.py

class ZombiePlayer():
    'handles player info'
    def __init__(self, name = input('Enter zombie name: \n')):
        self.name = name
        self.brains = 0
        self.shotguns = 0
        self.dice = [0, 0, 0]

    def display_dice(self):
        'display the players current dice'
        print(f'Green dice: {self.dice[0]}'.rjust(24))
        print(f'Yellow dice: {self.dice[1]}'.rjust(24))
        print(f'Red dice: {self.dice[2]}'.rjust(24))

    def update_scores(self, dice_roll):
        'takes a dice roll and updates the players values'
        self.dice = [0, 0, 0]
        self.brains += dice_roll['b']
        self.shotguns += dice_roll['s']
        for _ in range(dice_roll['f']['g']):
            self.dice[0] += 1
        for _ in range(dice_roll['f']['y']):
            self.dice[1] += 1
        for _ in range(dice_roll['f']['r']):
            self.dice[2] += 1

    def display_score(self):
        'show current score'
        print(f'Brains: {self.brains}'.rjust(24))
        print(f'Shotguns: {self.shotguns}'.rjust(24))

    def player_dice_amount(self):
        'returns the sum of the players current dice'
        return sum(self.dice)
