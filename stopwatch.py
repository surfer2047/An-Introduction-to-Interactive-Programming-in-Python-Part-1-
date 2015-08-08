# template for "Stopwatch: The Game"
import simplegui

# define global variables
msec = 0
sec = 0 
minute = 0
sec0 = 0
sec1 = 0
time = "0"



# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    global msec, sec, minute, sec0, sec1, time
    
    ms_100 = t % 10
   
    if ms_100 == 9:
        sec = sec + 1
        sec0 = sec % 10
        sec1 = sec / 10
        
        
    if sec == 59:
        minute = minute + 1
        sec = 0
        
    time = str(minute) + ":" + str(sec1)+str(sec0) + ":" + str(ms_100)
    
    
    
    

def ms_100():
    global msec
    #print msec
    msec = msec + 1
    format(msec)
    

    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()
    

def stop():
    timer.stop()
    
    
def reset():
    global msec, sec, sec0, sec1, minute, time
    msec = 0
    sec = 0
    sec0 = 0
    sec1 = 0
    minute = 0
    time = "0:00:0"
    timer.stop()
    

   
#define event handler for timer with 0.1 sec interval

def timer_handler():
    ms_100()

# define draw handler

def draw_handler(canvas):
    canvas.draw_text(time, (100, 100), 32, 'orange')
    canvas.draw_text("x/y", (230, 30), 32, 'orange')

    
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
timer.start()
                            


# Please remember to review the grading rubric


