import turtle
import colorsys as cs
turtle.setup(400,400)
turtle.speed(0)
turtle.tracer(10)
turtle.width(2)
turtle.bgcolor("black")
for j in range(12):
    for i in range(7):
        turtle.color(cs.hsv_to_rgb(i/7,j/12,1))
        turtle.right(90)
        turtle.circle(200-j*4.90)
        turtle.left(90)
        turtle.circle(200-j*4.90)
        turtle.right(160)
        turtle.circle(50.24)
turtle.hideturtle()
turtle.done()