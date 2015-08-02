#!/usr/bin/env python
# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)
count = 0

# Define "helper" functions

def increment():
    global count #This is global variable
    count = count + 1
    

def reset():
	global count
	count = 0

# Define event handler functions
def tick():
    increment()
    print count
    

# Create a frame

frame = simplegui.create_frame("simple Gui Test", 100, 100)

# Register event handlers
timer = simplegui.create_timer(1000, tick) 
frame.add_button("Click me", reset)

# Start frame and timers
frame.start()
timer.start()

