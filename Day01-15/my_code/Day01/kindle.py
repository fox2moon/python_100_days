"""
@Time : 2020/3/28 17:38
@Author: zhangqian
"""

from turtle import *

t = Turtle()
w = Screen()


def head():
     # tt = cos(t.radians(t.heading() + 45)) / 8 + 0.25
     t.circle(50, 200)
     print(t.pos())
     t.pensize(2)
     t.goto(-10, 110)
     print(t.pos())
     t.goto(-17.10, 96.98)
     # t.left(90)
     t.circle(40, 200)



def setting():
    """设置参数"""
    t.pensize(4)
    # 隐藏海龟
    # t.hideturtle()
    w.colormode(255)
    t.color((255, 155, 192), "black")
    w.setup(840, 500)
    # t.speed(5)


if __name__ == '__main__':
    """主函数"""
    setting()
    head()
    done()
