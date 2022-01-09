#! /usr/lib/python3
'handles dice in zombie game'

# .lib/game_dice.py

import random

class GameDice():
    'handling of the game dice'
    def __init__(self, green_dice = 6, yellow_dice = 4, red_dice = 3):
        self.green_dice = green_dice
        self.yellow_dice = yellow_dice
        self.red_dice = red_dice

    def dice_in_pool(self):
        'shows what dice are in the pool'
        print(f'Green dice: {self.green_dice}')
        print(f'Yellow dice: {self.yellow_dice}')
        print(f'Red dice: {self.red_dice}')

    def pick_dice(self, player_dice):
        'get a random dice until 3 dice'
        if self.green_dice + self.yellow_dice + self.red_dice + sum(player_dice) < 3: return False

        while sum(player_dice) < 3:
            total_dice = self.green_dice + self.yellow_dice + self.red_dice
            new_dice = random.randint(1, total_dice)

            if new_dice < self.green_dice:
                self.green_dice -= 1
                player_dice[0] += 1
            elif new_dice < self.green_dice + self.yellow_dice:
                self.yellow_dice -= 1
                player_dice[1] += 1
            elif new_dice < total_dice:
                self.red_dice -= 1
                player_dice[2] += 1
        return player_dice

def roll_green():
    'handles rolls of green dice'
    result = random.randint(1, 6)
    if result == 1:
        return 's'
    if result <= 3:
        return 'f'
    return 'b'

def roll_yellow():
    'handles rolls of yellow dice'
    result = random.randint(1, 6)
    if result <= 2:
        return 's'
    if result <= 4:
        return 'f'
    return 'b'

def roll_red():
    'handles rolls of red dice'
    result = random.randint(1, 6)
    if result <= 3:
        return 's'
    if result <= 5:
        return 'f'
    return 'b'

def roll_dice(player_dice):
    '''pass amount of each dice
    returns a dictionary: {'s': 0, 'f': {'g': 0, 'y': 0, 'r': 0}, 'b': 0}
    stores the color of footstep dice
    returns false if given wrong amount of dice'''
    if player_dice[0] + player_dice[1] + player_dice[2] != 3: return False

    dice_results = {'s': 0, 'f': {'g': 0, 'y': 0, 'r': 0}, 'b': 0}
    for _ in range(player_dice[0]):
        roll = roll_green()
        if roll == 'f':
            dice_results['f']['g'] += 1
        else:
            dice_results[roll] += 1
    for _ in range(player_dice[1]):
        roll = roll_yellow()
        if roll == 'f':
            dice_results['f']['y'] += 1
        else:
            dice_results[roll] += 1
    for _ in range(player_dice[2]):
        roll = roll_red()
        if roll == 'f':
            dice_results['f']['r'] += 1
        else:
            dice_results[roll] += 1
    return dice_results

