'''
Grace Bero & Abby Maahs
Final Project Hangman

Requirements Met:
1. Variables
2. Comments
3. If statement
4. Complex boolean condition
5. Getting input from user
6. Printing output to the console
7. Using +=
8. Nested if-statement
9. A graphics window
10. Uses a random number
11. Uses at least 1 user-defined function
12. Docstring in each function
13. Reading from a file
12. List
13. Global variables
14. Local variables
15. While Loop
16. For Loop

Instructions:
Click Run 
'''


from graphics import *
import random

hangman = GraphWin("Hang Man", 480, 480)
hangman.setCoords(0,0,1,1)
    
def board():
    """
    This will display the empty hangman board
    
    Parameters:
        NA
    Returns:
        hangman: The window for the graphics
        block1: The long line on the right
        block2: The line going across the top 
        block3: The noose
        block4: The floor
    """
    block1 = Rectangle(Point(0.60, 0.20), Point(0.61, 0.80))
    block1.draw(hangman)
    block1.setFill("black")

    block2 = Rectangle(Point(0.30, 0.79), Point(0.60, 0.80))
    block2.draw(hangman)
    block2.setFill("black")

    block3 = Rectangle(Point(0.30, 0.79), Point(0.31, 0.70))
    block3.draw(hangman)
    block3.setFill("black")

    block4 = Rectangle(Point(0.30, 0.20), Point(0.65, 0.19))
    block4.draw(hangman)
    block4.setFill("black")

infile = open('Python_words.csv', 'r')
word_list = infile.read().splitlines()

def pick_word():
    """
    Picks a word from a list of words
    
    Parameters:
        
    Returns:
        word: the random word chosen from the list
    """
    word = random.choice(word_list)
    return word.upper()

def instructions():
    """
    Prints the instructions
    
    Parameters:
        NA
    Returns:
        Printed lines of text
    """
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Lets Play Hangman ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("The goal of the game is to guess the word letter by letter before the man dies.")
    print("You will guess a letter")
    print("- If the letter is in the word, it will be added to the board")
    print("- If the letter is not in the word, a body part will be added to the man")
    print("- If the body is completed, you lose")
    print("- If you guess the word before then, You Win!")
    print()
    print("Guess the word and he will live, fail and he will die")
    print("Are you up for the challenge?")
    print("<><><><><><><><><><><><><><><><><><><><><><><><><>") 

def user_interaction(word):
    """
    Runs the game loop
    
    Parameters:
        word: A randomlly chosen word from a list of python related words
    Returns:
        guessed_letters: A list of already guessed letters
        word_letters: A list with '_' that will be replaced with the letters in the word as they are guessed
        head: Head of the hangman
        body: body of the hangman
        LArm: Left Arm of the hangman
        RArm: Right arm of the hangman
        LLeg: Left Leg of the hangman
        RLeg: Right Leg of the hangman
        
    """
    board()
    instructions()
    attempts = 0
    guessed_letters = []
    letters = list(word)
    word_letters = [] #list of _ for each letter in word
    guessed = False
    
    for i in range(len(word)):
        word_letters.append('_') #to create the _

    while attempts < 6 and not guessed:
        print("Your word has", len(word_letters), "letters: ", word_letters) 
        guess = input("Guess a letter: ").upper()
        print("<><><><><><><><><><><><><><><><><><><><><><><><><>") 
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that")
            elif guess not in word:
                print(guess, "is not in the word")
                guessed_letters.append(guess)
                attempts += 1
                if attempts == 1:
                    head = Circle(Point(0.305,0.65), 0.05)
                    head.setFill("purple")
                    head.draw(hangman)
                elif attempts == 2:
                    body = Line(Point(0.305,0.60,), Point(0.305, 0.4))
                    body.setOutline("purple")
                    body.draw(hangman)
                elif attempts == 3:
                    LArm = Line(Point(.205, .45), Point(.305, .55))
                    LArm.setOutline("purple")
                    LArm.draw(hangman)
                elif attempts == 4:
                    RArm = Line(Point(.305, .55), Point(.405, .45))
                    RArm.setOutline("purple")
                    RArm.draw(hangman)
                else:
                    LLeg = Line(Point(.305, .4), Point(.20, .25))
                    LLeg.setOutline("purple")
                    LLeg.draw(hangman)   
            else:
                print(guess, "is in the word")
                for ndx in range(len(letters)): #to change the _ to letter
                    if guess == letters[ndx]:
                        word_letters[ndx] = guess
        else:
            print("That answer is invalid, try again")
       
        print("Guessed Letters: ", guessed_letters)
        
        if '_' not in word_letters:
            guessed = True
            print("You guessed it, Good Job!")


    if attempts == 6:
        if not guessed:
            RLeg = Line(Point(.305, .4), Point(.405, .25))
            RLeg.setOutline("purple")
            RLeg.draw(hangman)
            print("Better Luck Next Time :( The word was ", word)
        else:
            print("You guessed it, Good Job!")
        
user_interaction(pick_word())
