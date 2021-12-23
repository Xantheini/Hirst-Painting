# Used to get colours from one of his paintings
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

color_list = [(187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242), (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27), (234, 171, 164), (162, 212, 176)]
t.colormode(255)
t.penup()
t.hideturtle()
t.goto(-250, -250)
t.speed(0)

for x in range(10):
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    t.goto(t.pos()[0] - 500, t.pos()[1] + 50)

t.Screen().exitonclick()
