###tree stuff
import turtle
from random import randint
wn = turtle.Screen()
wn.clearscreen()
bob=turtle.Turtle()
bob.left(90)
treeSize = input("treeSize Here: ")
treeSize = int(treeSize)
bob.backward(treeSize)
bob.speed(300)

def branch0(treeSize, n):
    if treeSize > 5:
        bob.pencolor('brown')
        bob.forward(treeSize)
        bob.right(20)
        branch0(treeSize-10, n)
        bob.pencolor('green')
        bob.left(40)
        branch0(treeSize-10, n)
        bob.right(20)
        bob.pencolor('green')
        branch0(treeSize-7, n)
        bob.pencolor('brown')
        bob.backward(treeSize)
def forest(d):
    for i in range(15):
        bob.penup()
        bob.goto(randint(-200,200), randint(-200,200))
        bob.pendown()
        branch0(treeSize,10)

#forest(3)
    
def drawTriangle(size):
    bob.forward(size)
    bob.right(120)
    drawTriangle(size-10)
    bob.forward(size)
    bob.right(120)
    drawTriangle(size-10)
    bob.forward(size)
    bob.right(120)
    drawTriangle(size-10)
    
drawTriangle(40)
    

    

