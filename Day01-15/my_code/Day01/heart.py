"""
@Time : 2020/3/30 13:45
@Author: zhangqian
"""

from turtle import *


def jumpto(x, y):
    t.up()
    t.goto(x, y)
    t.down()


t = Turtle()
w = Screen()

w.setup(800, 800)
t.left(90)
t.pensize(5)
t.pencolor("red")
t.fillcolor("red")
t.begin_fill()
t.circle(50, 200)
t.goto(0, -120)
jumpto(0, 0)
t.setheading(90)
t.circle(-50, 200)
t.goto(0, -120)
t.end_fill()
t.hideturtle()
t.done()
