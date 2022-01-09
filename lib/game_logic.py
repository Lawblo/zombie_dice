#! /usr/lib/python3

# .lib/new_game.py

import zombie_player
import game_dice

def turn(player, game):
    'one turn'
    player.dice = game.pick_dice(player.dice)
    roll = game_dice.roll_dice(player.dice)
    player.update_scores(roll)

zombie = zombie_player.ZombiePlayer()
dice = game_dice.GameDice()

zombie.display_score()
turn(zombie, dice)
zombie.display_score()
