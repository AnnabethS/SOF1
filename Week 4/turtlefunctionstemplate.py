'''
Created on 24 Jul 2020

@author: Lilian
'''

import turtle
import math
my_turtle = turtle.Turtle()
my_turtle.showturtle()

####################      WRITE YOUR CODE BELOW      #########################

# my_turtle.speed(1)

def draw_triangle(size):
    my_turtle.penup()
    my_turtle.goto(0,size/2)
    my_turtle.pendown()
    my_turtle.right(60)
    my_turtle.forward(size)
    my_turtle.right(120)
    my_turtle.forward(size)
    my_turtle.right(120)
    my_turtle.forward(size)
    my_turtle.right(60)
    my_turtle.penup()
    my_turtle.goto(0,0)

for i in range(10):
    draw_triangle((i+1)*20)

# draw_triangle(10)
#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()
