#Snake Game
import turtle
import time

delay = 0.1

#set up the screen
window = turtle.Screen()
window.title("Snake Game by @QuangDaoNgo") #game title
window.bgcolor("black") #background color
window.setup(width=600, height=600) #size of the screen
window.tracer(0) #turns of the screen updates

#create the snake head
head = turtle.Turtle()
head.speed(0) #set to 0 because it is the fastest animation, as fast as possible
head.shape("square") #set the head shape (it can be 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic')
head.color("white")
head.penup() #the python turtle is keeping drawing the line so using penup could stop drawing any line
head.goto(0,0) #start at the center of the screen
head.direction = "right" #head going to seat there in the middle

#functions
def move_up():  
    head.direction == "up"
def move_down():
    head.direction == "down" 
def move_right():
    head.direction == "right"
def move_left():
    head.direction == "left"

def move():
    if head.direction == "up": #control the snake to move up
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down": #control the snake to move down
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right": #control the snake to move right
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left": #control the snake to move left
        x = head.xcor()
        head.setx(x - 20)


#main game loop
while True:
    window.update()  #everytime go through the loop, this update the screen
    move()
    time.sleep(delay)
    
  
#keep the window open
window.mainloop() 