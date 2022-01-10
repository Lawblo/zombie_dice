
# Zombie Dice Bots

## Dice

13 dice
Different kinds of dice: red, green, and yellow

3 red: 2 footsteps, 3 shotgun, 1 brain
6 green: 2 footsteps, 1 shotgun, 3 brains
4 yellow: 2 footseps, 2 shotgun, 2 brains

## RULES

Always roll 3 dice
Can roll until used all 13 dice or 3 shtgn blasts

**Shotgun** => 3: discard brains and end turn

**Brains** => 1 point per at end of turn

**Footsteps** => Set aside brains and shotgun dice, draw until 3 dice and reroll if continue.

When someone reaches 13 brains:
  End game after round
  Winner is most brains
  If tie, tied players play one last tiebraker round

## TURN

``` ruby

Draw until 3 dice

Roll dice

Add results

if 3 shtgn          => end turn with 0 points

else                => decide to end or continue

if all dice rolled  => end and count brains

if end              => count brains

if continue         => save and remove brains and shotguns, keep footsteps

if enough dice left => add until 3 dice

```

## Possible bots

- A bot that, after the first roll, randomly decides if it will continue or stop
- A bot that stops rolling after it has rolled two brains
- A bot that stops rolling after it has rolled two shotguns
- A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
- A bot that stops rolling after it has rolled more shotguns than brains
