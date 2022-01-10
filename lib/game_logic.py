#! /usr/lib/python3
'handles the flow of the game'

# .lib/new_game.py

import zombie_player
import game_dice
import bot_zombies

def turn(player, game):
    'turn handler'
    while True:
        player.rolls += 1
        forced_end = check_forced_end_game(player, game)
        if forced_end is True:
            break
        if player.rolls != 1:
            # player_cont = check_player_end_game()
            player_cont = bot_zombies.two_brains(player)
            if player_cont is False:
                break
        # print(f'\nROLL {player.rolls}:\n')
        player.dice = game.pick_dice(player.dice)
        # print('Dice pulled: ')
        # player.display_dice()
        # print('\nROLLING DICE ...\n')

        roll = game_dice.roll_dice(player.dice)
        # display_roll_outcome(roll)
        player.update_scores(roll)
        # display_game_standings(player, game)

    display_end_points(player)
    return player.brains

def check_forced_end_game(player, game):
    'Returns True if theres not enough dice left to continue the round'
    if (player.player_dice_amount() + game.dice_left()) < 3:
        # print('Not enough dice to continue! Round over.')
        return True
    if (player.shotguns) > 2:
        # print('Collected 3 shotguns! GAME OVER!')
        player.brains = 0
        return True
    return False

def check_player_end_game():
    'Returns true if the player wishes to continue'
    while True:
        player_choice = input("Continue?\nEnter 'y' to continue, or 'n' to give up:  ")
        if player_choice == 'y':
            return True
        if player_choice == 'n':
            return False
        print('Wrong input')

# def check_ai_end_game(player, game, bot):
#     'checks if the bot wants to continue'
#     #bot(player, game)
#     bot(game, player)

def display_roll_outcome(roll):
    'display current roll'
    print('You rolled: ')
    print('------------------------')
    for _ in range(roll['s']):
        print('***SHOTGUN***'.rjust(24))
    for _ in range(roll['f']['g']):
        print('Green footsteps'.rjust(24))
    for _ in range(roll['f']['y']):
        print('Yellow footsteps'.rjust(24))
    for _ in range(roll['f']['r']):
        print('Red footsteps... oh oh!'.rjust(24))
    for _ in range(roll['b']):
        print('BRAAAAAIIIIINSSS'.rjust(24))
    print('------------------------')
    print()

def display_game_standings(player, game):
    'displays info about the current game'
    print('Current points:'.ljust(24))
    player.display_score()
    print()
    print('Dice in hand:'.ljust(24))
    player.display_dice()
    print('\nDice left in game:'.ljust(24))
    game.dice_in_pool()

def display_end_points(player):
    'shows score at end of game'
    print(f'Player {player.name}:')
    print(f'Brains collected: {player.brains}')

# zombie = zombie_player.ZombiePlayer('COMPUTER')
# dice_game = game_dice.GameDice()

TURN_BRAINS = 0
PLAY_TIMES = 10
for i in range(PLAY_TIMES):
    TURN_BRAINS += turn(zombie_player.ZombiePlayer('COMPUTER'), game_dice.GameDice())

print(TURN_BRAINS/PLAY_TIMES)
