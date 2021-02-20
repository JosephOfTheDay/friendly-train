import math


i=input("what tempature would you like the water to be?:   ")
i=int(i)
def stateOfWater(i):
    if i >=212:
        print("the water is beggining to turn into gas!")
    elif i <=32:
        print('The water is beggingin to freeze, or is already frozen')
    elif i >32<212:
        print("The water is in a liquid state!")
stateOfWater(i)


import turtle
import math

screen=turtle.Screen()
screen.clearscreen()
b=turtle.Turtle()
b.penup()
b.goto(-150,150)
b.speed(10)
tl=input("what color for the traffic light?:   ")
b.speed(100)

def tlColor(tl):
    drawMain()
    if tl == 'green':
        drawRed(False)
        drawYellow(False)
        drawGreen(True)
    elif tl == 'red':
        drawRed(True)
        drawYellow(False)
        drawGreen(False)
    elif tl == 'yellow':
        drawRed(False)
        drawYellow(True)
        drawGreen(False)
    
        
def drawMain():
    b.fillcolor(0,0,0)
    b.begin_fill()
    b.pendown()
    b.forward(50)
    b.right(90)
    b.forward(200)
    b.right(90)
    b.forward(50)
    b.right(90)
    b.forward(200)  
    b.end_fill()


def drawRed(on):
    b.right(90)
    b.right(90)
    b.forward(50)
    if on == True:
        b.fillcolor('red')
    else:
        b.fillcolor("red4")
    b.begin_fill()
    b.circle(25)
    b.end_fill()

def drawYellow(on):
    b.forward(50)
    if on == True:
        b.fillcolor('yellow')
    else: 
        b.fillcolor("LightYellow")
    b.begin_fill()
    b.circle(25)
    b.end_fill()

def drawGreen(on):
    b.forward(50)
    if on == True:
        b.fillcolor('green')
    else:
        b.fillcolor("LightGreen")
    b.begin_fill()
    b.circle(25)
    b.end_fill()

tlColor(tl)