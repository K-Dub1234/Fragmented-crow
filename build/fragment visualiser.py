import turtle
import random as r
import __init__ as i
words=[]
num=0
speed=0.8
screen = turtle.Screen()
screen.bgcolor('black')
screen.tracer(0)            

t = turtle.Turtle()
t.speed(200)
t.width(3)
t.hideturtle()            

def write(x) :

    t.color('white')
    t.write(x, font=('arial', 20, 'normal'))
t.penup()
t.goto(-350, 0)
t.pendown()

def run():
    words=[num]
    t.clear()
    write(words)
    screen.update()         
    t.forward(speed)

while speed != 0:
    run()
    tx= t.xcor()
    print(tx + '   ', IP)
    num=ip
    i.setupKIplus(r.randint(1111, 9999))
    if tx == 306.000000000005:
        i.setupKIplus(r.randint(1111, 9999))
        num=ip
        t.clear()
        t.goto(-350, 0)
        run()
        


