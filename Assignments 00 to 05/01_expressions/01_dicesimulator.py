# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. 
# This program is used to show how variable scope works.

import random

NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints the results of each roll.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    print(f"Rolled dice: {die1}, {die2} (Total: {die1 + die2})")

def main():
    print("Rolling two dice three times...")
    roll_dice()
    roll_dice()
    roll_dice()

if __name__ == '__main__':
    main()
