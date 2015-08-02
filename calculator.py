#!/usr/bin/env/python
#Author: @nix1947

#import simplegui
import simplegui

#Defining global variable

store = 12
operand = 3

#Defining helper functions, never call helper function from event handler

#Defining handler function

def output():
    """Display the output """
    global store, operand
    print "Store =", store
    print "Operand=", operand

def swap():
    """Swap the Operand and store"""
    global store, operand
    store, operand = operand, store
    output()

def add():
    """Add store and operand and save in store"""
    global store, operand
    store = store + operand
    output()

def divide():
    """Divide the operand by store """
    global store, operand
    store = store / operand
    output()

def subtract():
    """Subtract the operand from store"""
    global store, operand
    store = store - operand
    output()

#Creating the canvas

frame = simplegui.create_frame("Calculator", 200, 200)
frame.add_button("Print", output, 100)  #Here 100 define the width of buttons
frame.add_button("swaptext", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Divide", divide, 100)
frame.add_button("subtract", subtract, 100)

#Start the frame
frame.start()

