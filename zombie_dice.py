#! /usr/bin/python3

# zombie_dice.py

import random

class ZombieDice():
    def __init__(self, player_name):
        self.name = player_name
        
    
class GameDice():
    def __init__(self, green_dice = 6, yellow_dice = 4, red_dice = 3):
        self.green_dice = green_dice
        self.yellow_dice = yellow_dice
        self.red_dice = red_dice

    def roll_green():
        result = random.randint(1, 6)
        if result == 1: return 0
        if result <= 3: return 1
        return 2

    def roll_yellow():
        result = random.randint(1, 6)
        if result <= 2: return 0
        if result <= 4: return 1
        return 2

    def roll_red():
        result = random.randint(1, 6)
        if result <= 3: return 0
        if result <= 5: return 1
        return 2

    def roll(green, yellow, red):
        if green + yellow + red != 3: return False

        dice_results = [0, 0, 0]
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

    def pick_dice(self, previous_dice = 0):
        if self.green_dice + self.yellow_dice + self.red_dice + previous_dice < 3: return False
        dice_pool = [self.green_dice, self.yellow_dice, self.red_dice]
        print(dice_pool)
        


test_dice = GameDice()

test_dice.pick_dice()
