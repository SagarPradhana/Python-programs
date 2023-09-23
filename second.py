import turtle as t
import colorsys
t.bgcolor("black")
t.speed(11)
t.right(45)
h=45
for n in range(250):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.045
    t.color(c)
    if 7<n<110:
        t.left(65)
    if 80<n<133:
        t.right(85)