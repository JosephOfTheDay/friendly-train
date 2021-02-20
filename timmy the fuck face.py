import turtle
import math



wn=turtle.Screen()
wn.bgcolor("black")
wn.clearscreen()
timmy=turtle.Turtle()
timmy.shape('turtle')
p = timmy.pencolor('blue')

def star():
    timmy.penup()
    
    timmy.goto(-80,0)
    
    timmy.pendown()
    
    i = 0
    while i ==0:
        timmy.pencolor('blue')
        timmy.right(10)
        timmy.forward(300)
        o = 1
        while o ==1:
            timmy.pencolor('blue')
            o=0
        o=0
        
        timmy.left(144)
        

        
star()