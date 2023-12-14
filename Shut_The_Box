'''
Shut the Box
Grace Bero
Abby Maahs
CS065 - Lab 13: Make a Dice Game
How to play: Hit Run
Criteria Hit:
    at least 1 list
    nested if-statement
    a single for loop (separate from a nested for loop)
    a nested for loop
    a while loop
    use the range() function
    at least 2 functions (other than roll_die)
'''
# Roll a dice
import random
 
 
def roll_die(num_sides):
    """
    Will return a random number between 1 and num_sides, as a dice would.
 
    Parameters:
        num_sides: the upper bound on the random number
    Return:
        a random number between 1 and num_sides, inclusive.
    """
    return random.randint(1, num_sides)
 
# Roll both dice
def roll_dice(num_dice, num_sides):
    """
    User inputs a number of dice and a number of sides for the dice and it will return
    2 random dice rolls
 
    Parameters:
        num_dice: int, Number of dice wanted
        num_sides: int, Number of sides the dice will have
    Returns:
        roll: list, len of num_dice and values ranging from 1 - num_sides
    """
    roll = []
    for x in range(num_dice): 
        roll.append(roll_die(num_sides))
    return roll
 
 
# List 2-12
value_list = [1, 2, 3, 4, 5, 6, 7]
 
 
# User input
def user_interaction(roll, rem_list): 
    """
    User decided which number to remove from the list. The value gets removed from the value list
 
    Args:
        roll: The list of the 2 dice roll results
        rem_list: The number removed from the list
 
    Returns:
 
    """
    removed_dice = input("Which dice would you like to remove? (If you cant remove a value enter 0): ")
    rem_list = []
    rem_list.append(int(removed_dice))
    if rem_list[-1] == sum(roll): 
        if rem_list[-1] in value_list: 
            value_list.remove(rem_list[-1])
            rem_list.remove(sum(roll))
    for i in range(len(value_list)): 
        for j in range(len(rem_list)): 
            if rem_list[j] == value_list[i]:
                value_list.remove(rem_list[j])
                rem_list.remove(rem_list[j])  # reference: Bestie Svetlana Greipel
 
 
# Instructions
def print_instructions():
    print("Instructions:")
    print("There is a list of numbers counting up from 1-7.")
    print("The goal of the game is to remove every single value from the list in the least amount of turns")
    print()
    print("Example: ")
    print("If you roll a 2 and a 3, you can remove 2, 3, or 5 from the list.")
 
# Gameplay
def play_game(roll):
    """
    When called it will play the game Shut the Box
 
    :param roll: list, len of num_dice and values ranging from 1 - num_sides
    :return:
    """
    num_dice = 2
    num_sides = 6
    counter = 0
 
    print("<><><><><><><><><><><><><><><>")
    print(print_instructions())
    print("<><><><><><><><><><><><><><><>")
 
    while len(value_list) > 0:
        p_roll = roll_dice(num_dice, num_sides)
        print("You Rolled: ", p_roll)
        print("The sum is: ", sum(p_roll))
        print("Current values left: ", value_list)
        user_interaction(roll, [])
        counter += 1
        print("<><><><><><><><><><><><><><><>")
    if len(value_list) == 0:
        print("It took you", counter, "rolls to shut the box")
        print("<><><><><><><><><><><><><><><>")
 
 
play_game([])
