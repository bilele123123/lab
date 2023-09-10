import random
# Generate an array of n size, and return the array sorted in descending order.
def roll_dice(dice):
    for i in range(len(dice)):
        dice[i] = random.randint(1, 6)
    dice.sort(reverse = True)
    return dice