import math


vowels = ["a","e","i","o","u"]
def sinvowel(word):
    word=str(word)
    print(len(word))
    w = len(word)
    w=int(w)
    l = word[0]

    if l == 'a':
        w= True
    elif l == 'e':
        w=True
    elif l == 'i':
        w=True
    elif l == 'o':
        w= True
    elif l == 'u':
        w=True
    else:
        w=False
    return(w)
n=input("Enter number here:   ")
n=int(n)
def isEven(n):
    if n%2==0:
        print("The number is even")
    else:
        print("The number is false")
isEven(n)
word=input("word:  ")
w = len(word)
print(w)
w=int(w)
word=[word]
def join_a_or_an_with(word):
    word=input("enter your word here:  ")
    
    if sinvowel(word):
        print("an" , str(word))
    else:
        print("a", str(word))
    
       
                    
join_a_or_an_with(word)
import turtle

import math

wn=turtle.Screen()
wn.clearscreen()
billy=turtle.Turtle()
billy.shape('square')
billy.color('green')
wn.bgcolor('white')

billy.penup()
billy.goto(0,0)


#create the cirlce
o=1
def circle():
    o=1
    for i in range(80):
        billy.pendown()
        billy.forward(10)
        billy.right(10)
        if billy.heading()%90==0:
            billy.pensize(5)
            billy.pencolor('red')
        else:
           billy.pensize(1)
           billy.pencolor('green')
           
circle()
billy.penup()
billy.forward(150)
billy.pendown()
def circle2():
    billy.color('blue')
    billy.pencolor('blue')
    o=1
    for i in range(80):
        billy.pendown()
        billy.forward(10)
        billy.right(10)
        if billy.heading()%330==0:
            billy.pensize(5)
            billy.pencolor('red')
        else:
           billy.pensize(1)
           billy.pencolor('blue')
        o=o+1
circle2()
def circle3():
    
    for i in range(500):
        billy.pendown()
        billy.forward(1)
        billy.right(1)
        if billy.heading()%30==0:
            billy.pensize(5)
            print("another hour has passed")
        else:
            billy.pensize(1)
billy.forward(120)
circle3()

