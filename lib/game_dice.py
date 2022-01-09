#! /usr/lib/python3

# .lib/game_dice.py

import random

class GameDice():
    def __init__(self, green_dice = 6, yellow_dice = 4, red_dice = 3):
        self.green_dice = green_dice
        self.yellow_dice = yellow_dice
        self.red_dice = red_dice


    # 0 = shotgun, 1 = footsteps, 2 = brains
    def roll_green():
        result = random.randint(1, 6)
        if result == 1: return 's'
        if result <= 3: return 'f'
        return 'b'
    def roll_yellow():
        result = random.randint(1, 6)
        if result <= 2: return 's'
        if result <= 4: return 'f'
        return 'b'
    def roll_red():
        result = random.randint(1, 6)
        if result <= 3: return 's'
        if result <= 5: return 'f'
        return 'b'

    # pass amount of each dice, returns a dictionary with outcome
    # returns false if given wrong amount of dice
    def roll(green, yellow, red):
        if green + yellow + red != 3: return False

        dice_results = {'s': 0, 'f': 0, 'b': 0}
        for i in range(green):            
            roll = GameDice.roll_green()
            dice_results[roll] += 1
        for i in range(yellow):            
            roll = GameDice.roll_yellow()
            dice_results[roll] += 1
        for i in range(red):            
            roll = GameDice.roll_red()
            dice_results[roll] += 1
        return dice_results


    def pick_dice(self, previous_dice = [0, 0, 0]):
        if self.green_dice + self.yellow_dice + self.red_dice + previous_dice < 3: return False
        dice_pool = [self.green_dice, self.yellow_dice, self.red_dice]