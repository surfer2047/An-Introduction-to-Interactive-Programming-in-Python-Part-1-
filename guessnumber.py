##!/usr/bin/env/python
#Author: @nix1947
#Description: Please run this code in codeskulptor.org
#Purpose: Creating the guessing number game

import simplegui
import math
import random

secret_number = 0
count = 7

# helper function to start and restart the game
def new_game():
    """Start new game, range is from 0 to 100 """
    
    print "New game, range is from 0 to 100"
    global secret_number
    global count 
    secret_number = random.randrange(0,100)
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    """Start new game, range is from 0 to 100 """
    
    print "New game, range is from 0 to 100"
    global count
    global secret_number
    count = 7
    secret_number = random.randrange(0,100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game   
    """Start new game, range is from 0 to 100 """

    print "New game, range is from 0 to 1000"
    global secret_number
    global count 
    count = 10
    secret_number = random.randrange(0,1000)
    
def input_guess(guess):
    """This will process the user input """
    
    global count
    if count == 0:
        print "You ran out of guesses"
        new_game()
    else:
        guess = int(guess)
        print "Guess was", guess
        print "Number of remaining Guesses", count-1
        if guess > secret_number:
            print "Lower!"
        elif guess < secret_number:
            print "Higher!"
        else:
            print "Correct!"
    count = count - 1
    print " "

# create frame

f = simplegui.create_frame("Guess Number", 200, 200, 200)

# register event handlers for control elements and start frame
f.add_input("Input Guess", input_guess, 200)
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

