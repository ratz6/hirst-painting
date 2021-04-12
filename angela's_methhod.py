import turtle as t
import random

t.colormode(255)
colour_list = [(248, 244, 235), (239, 250, 245), (250, 240, 246), (233, 241, 247), (133, 167, 191), (210, 155, 104), (29, 111, 162), (197, 144, 167), (233, 215, 86), (126, 74, 92), (27, 136, 68), (185, 176, 22), (60, 18, 26), (169, 71, 47), (225, 171, 197), (134, 21, 37), (113, 189, 140), (44, 173, 116), (37, 17, 16), (227, 85, 53), (233, 217, 7), (184, 92, 110), (9, 101, 52), (39, 169, 184), (21, 23, 31), (186, 185, 208), (146, 218, 168), (235, 171, 159), (155, 208, 216), (140, 23, 17)]
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed('fastest')
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
n = 100
for i in range(1, n+1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if (i % 10) == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)








screen = t.Screen()
screen.exitonclick()