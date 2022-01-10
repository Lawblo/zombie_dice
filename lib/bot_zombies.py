#! /usr/lib/python3
'bots for the game zombie dice'

# .lib/bot_zombies

import random

def random_choice(_player):
    'random selection of continue, dont continue'
    if random.randint(1,2) == 1:
        return True
    return False

def two_brains(player):
    'A bot that stops rolling after it has rolled two brains'
    if player.brains >= 2:
        print(f'Brains: {player.brains}')
        return True
    return False

def two_shotguns(player):
    'A bot that stops rolling after it has rolled two shotguns'
    if player.shotguns >= 2:
        return True
    return False

def random_stop_two_shotgun(player):
    '''A bot that initially decides it'll roll the dice one to four times,
    but will stop early if it rolls two shotguns'''
    play_times = random.randint(1, 4)
    if player.rolls > play_times:
        return True
    if player.shotguns >= 2:
        return True
    return False



def more_shotguns_than_brains(player):
    'A bot that stops rolling after it has rolled more shotguns than brains'
    if player.shotguns > player.brains:
        return True
    return False
