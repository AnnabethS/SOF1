'''
Created on 24 Jul 2020

@author: Lilian
'''

import turtle
import math
my_turtle = turtle.Turtle()
my_turtle.showturtle()

####################      WRITE YOUR CODE BELOW      #########################

my_turtle.speed(100)

def draw_star(size):
    my_turtle.setheading(90)
    draw_triangle(size)
    my_turtle.setheading(270)
    draw_triangle(size)

def draw_triangle(size):
    triangleHeight = (size/2) * math.sqrt(3)
    my_turtle.penup()
    my_turtle.forward(triangleHeight * 0.65)
    my_turtle.left(30)
    my_turtle.pendown()
    for i in range(3):
        my_turtle.left(120)
        my_turtle.forward(size)
    my_turtle.right(30)
    my_turtle.penup()
    my_turtle.back(triangleHeight * 0.65)
    
        


for i in range(6):
    if(i%2 == 0):
        draw_star(50 * (i+1))


#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()