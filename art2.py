import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
t.pensize(4)
h=0
t.up()
t.goto(50, -150)
t.down()
for i in range(500):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.1
    t.color('black')
    t.fillcolor(c)
    t.up()
    t.circle(i,45)
    t.down()
    t.begin_fill()
    t.fillcolor()
    t.circle(80,120)
    t.left(88)
    t.circle(80,145)
    t.end_fill()
t.done()