# template for "Stopwatch: The Game"
#Author: nix1947
#Purpose:Stopwatch game, assignment of coursera mini-project 3
#Description: Try to stop the watch at 100 ms, if you stop, you will get the point, run this project in codeskulptor.org

import simplegui

# define global variables
msec = 0
start = False
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):    
    totalsecond = t / 10
    minute = totalsecond / 60
    remainsecond = totalsecond % 60
    tenth_sec = t % 10
    if remainsecond < 10 and minute < 10:
        return "0" + str(minute) + ":" + "0" + str(remainsecond) + ":" + str(tenth_sec)
    else:
        return  str(minute) + ":" + str(remainsecond) + ":" + str(tenth_sec)
        
def ms_100():
    global msec
    msec = msec + 1
  
#define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global start
    timer.start()
    start = True
    
def stop():
    global x, y, start
    if start == True:
        y +=1    
    if msec % 10 == 0 and start == True:
        x += 1
    timer.stop()
    start = False
    
def reset():
    global msec, x, y, start
    msec = 0
    x=0
    y=0
    timer.stop()
    start = False
   
#define event handler for timer with 0.1 sec interval

def timer_handler():
    ms_100()

# define draw handler

def draw_handler(canvas):
    canvas.draw_text(format(msec), (100, 100), 40, 'white')
    canvas.draw_text(str(x) + "/" + str(y), (230, 30), 32, 'orange')
 
# create frame
frame = simplegui.create_frame("Stop watch", 300, 300 )

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()


