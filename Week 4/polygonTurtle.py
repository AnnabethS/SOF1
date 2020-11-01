'''
Created on 24 Jul 2020

@author: Lilian
'''

import turtle
import math
my_turtle = turtle.Turtle()
my_turtle.showturtle()

####################      WRITE YOUR CODE BELOW      #########################
SIZE = 75

def drawPolygon(sides):
    angle = 180 - (360/sides)
    for i in range(sides):
        my_turtle.forward(SIZE)
        my_turtle.right(180 - angle)

drawPolygon(13)

#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()