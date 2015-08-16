#!/usr/bin/env python
#Author: @nix1947
#Description: Coursera Implementation of PONG Game
#Run this game in code skulptor
# Implementation of classic arcade game Pong
# Implementation of classic arcade game Pong
#URL: http://www.codeskulptor.org/#user40_8Iq7vbEY4yTLxKR.py

# Implementation of classic arcade game Pong

#!/usr/bin/env python
#Author: @nix1947
#Description: Coursera Implementation of PONG Game
#Run this game in code skulptor
# Implementation of classic arcade game Pong
#http://www.codeskulptor.org/#user40_ayZsNerVu4ZLB3x.py
# Implementation of classic arcade game Pong

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddels
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddel1_pos =  HEIGHT/2
paddel2_pos =  HEIGHT/2
paddel1_vel = 0
paddel2_vel = 0
ball_pos = [WIDTH/2, HEIGHT/2] #place ball at the center of the position
#store horizontal velocity and vertical velocity
ball_vel = [0, 0]
score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel       # these are vectors stored as lists  
   
    if direction: # if the ball is at left side, reverse it  and push upward     
        ball_vel[0] = random.randrange (120, 240) / 60.0
        ball_vel[1] = random.randrange (60, 120) / 60.0
    else: #if the ball is at right side reverse it and push upward
        ball_vel[0] = -random.randrange (120, 240) / 60.0
        ball_vel[1] = -random.randrange (60, 120) / 60.0
    
 
#define event handlers
def new_game():
    global paddel1_pos, paddel2_pos, paddel1_vel, paddel2_vel  # these are numbers
    global score1, score2  # these are ints
    paddel1_pos =  HEIGHT/2
    paddel2_pos =  HEIGHT/2
    paddel1_vel = 0
    paddel2_vel = 0
    spawn_ball(LEFT)
    
    

def draw(canvas):
    global score1, score2, paddel1_pos, paddel2_pos, ball_pos, ball_vel, paddel1_vel, paddel2_vel
   
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
  
    
    #check for the ball collision with gutter
    
    if ball_pos[0] <= BALL_RADIUS: #If collide in left push right
       
        #check for the paddel1 strike 
        if ball_pos[1] >= paddel1_pos - PAD_HEIGHT / 2 and ball_pos[1] < paddel1_pos + PAD_HEIGHT /2:
            print "Strike"
            score1 += 1
            ball_vel[0] += ball_vel[0] * 0.10 #when touch to paddel increase velcocity along by 10 %
            ball_vel[1] += ball_vel[1] * 0.10 #when touch to paddel increase velcocity along by 10 %
        else:
            ball_pos = [WIDTH/2, HEIGHT/2] #if touch to gutter reset the ball to center position
            
        spawn_ball(RIGHT) #The ball has been strike to LEFT push it to RIGHT DIRECTION
        
    
    if ball_pos[0] >= WIDTH - BALL_RADIUS: # if the ball collide to right side, push to left
         #check for the paddel2 strike 
        if ball_pos[1] >= paddel2_pos - PAD_HEIGHT / 2 and ball_pos[1] < paddel2_pos + PAD_HEIGHT /2:
            print "Strike"
            score2 += 1
            ball_vel[0] +=  ball_vel[0] * 0.10 #when touch to paddel increase velcocity along by 10 %
            ball_vel[1] +=  ball_vel[1] * 0.10 #when touch to paddel increase velcocity along by 10 %
        else:
            ball_pos = [WIDTH/2, HEIGHT/2]
        spawn_ball(LEFT)
     
    if ball_pos[1] <= BALL_RADIUS:
         ball_vel[1] = -ball_vel[1] #move the ball downwards
    
    
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1] # move the ball upwards
 
    paddel_range = [ paddel1_pos - PAD_HEIGHT // 2, paddel1_pos + PAD_HEIGHT // 2]
    
    
     # update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #check for the ball collision with paddel
    
    print ball_vel
    
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')
    
    
    # update paddel's vertical position, keep paddel on the screen
    paddel1_pos += paddel1_vel
    paddel2_pos += paddel2_vel
    
    # stop paddel 1 when reaches to the corner of the canvas
    if paddel1_pos <= 40:
        paddel1_vel = 0
        paddel1_pos = 40
    if paddel1_pos >= 360:
        paddel1_vel = 0
        paddel1_pos = 360
    
    #stop paddel 2 when reaches to the corner of the canvas
    
    if paddel2_pos <= 40: #End of the corner is equal to ( 0 + 
        paddel2_vel = 0
        paddel2_pos = 40
    if paddel2_pos >= 360:
        paddel2_vel = 0
        paddel2_pos = 360
      
    
    # draw paddel 1
    canvas.draw_line([0, paddel1_pos-PAD_HEIGHT/2],[0,paddel1_pos+ PAD_HEIGHT/2], PAD_WIDTH *2, "white")
    
    #draw paddel 2
    canvas.draw_line([WIDTH, paddel2_pos-PAD_HEIGHT/2],[WIDTH,paddel2_pos+ PAD_HEIGHT/2], PAD_WIDTH *2, "white")
    
    
    
    # determine whether paddel and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), (250,50), 24, "White")
    canvas.draw_text(str(score2), (350,50), 24, "White")
        
def keydown(key):
    global paddel1_vel
    global paddel2_vel
    # w and s control the vertical velocity of paddel 1, LEFT PADDEL
  
    if key == simplegui.KEY_MAP['w']:
        paddel1_vel += -5
    if key == simplegui.KEY_MAP['s']:
        paddel1_vel += 5
    if key == simplegui.KEY_MAP['up']:
        paddel2_vel += -5
    if key == simplegui.KEY_MAP['down']:
        paddel2_vel += 5
   
    
     
    
    # uparrow and down arrow control the vertical velocity of paddel 2 RIGHT PADDEL
   

def keyup(key):
    global paddel1_vel, paddel2_vel, paddel1_pos, paddel2_pos
   
    # w and s control the vertical velocity of paddel 1, LEFT PADDEl
    if key == simplegui.KEY_MAP['w']:
        paddel1_vel = -1
    if key == simplegui.KEY_MAP['s']:
        paddel1_vel = 1
    # uparrow and down arrow control the vertical velocity of paddel 2 RIGHT PADDEL
    if key == simplegui.KEY_MAP['up']:
        paddel2_vel = -1
    if key == simplegui.KEY_MAP['down']:
        paddel2_vel = 1
    else:
        pass


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game)


# start frame
new_game()
frame.start()

