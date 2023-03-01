from turtle import Turtle, Screen
import turtle
import random
import colorgram

kleon = Turtle()
turtle.colormode(255)
kleon.shape("turtle")
kleon.color("chartreuse")
kleon.penup()
kleon.hideturtle()
color_tups = []
kleon.pensize(10)

## Extract colors from a specific painting ##
# for num in range(20):
#     colors = colorgram.extract('hirst_dot_painting_01.jpg', 20)
#     current_color = colors[num]
#     rgb = current_color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     color_tuple = (r, g, b)
#     color_tups.append(color_tuple)
#
# print(color_tups)


## My own Million $$$ turtle dot painting

# Extracted color list
color_list = [(248, 242, 233), (247, 142, 68), (251, 66, 121), (153, 159, 52), (3, 142, 83), (250, 73, 57),
              (155, 44, 86), (214, 237, 232), (251, 223, 228), (249, 225, 69), (2, 133, 174), (4, 196, 220),
              (106, 45, 97), (158, 50, 48), (206, 234, 237), (236, 106, 154), (91, 191, 206), (116, 187, 154),
              (4, 119, 46), (247, 166, 153)]
y = -250
x = -250
kleon.speed("fastest")
for _ in range(10):
    kleon.penup()
    kleon.goto(x, y)
    for _ in range(10):
        rand_num = random.randint(0, len(color_list) - 1)
        kleon.dot(20, color_list[rand_num])
        kleon.forward(50)
        y += 5




















### 2

## Draw a Spirograph ##

# RANDOM COLORS AND RANDOM DIRECTIONS##
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb_tuple = (r, g, b)
#     return rgb_tuple

# kleon.speed("fastest")
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         kleon.circle(100)
#         kleon.setheading(kleon.heading() + size_of_gap)
#         kleon.pencolor(random_color())
#
# draw_spirograph(5)


### 1

## Draw a random colored line in a random direction
# random_range = 200
# for _ in range(random_range):
#     kleon.speed("fastest")
#     kleon.pensize(10)
#     directions = [0, 90, 180, 360]
#     kleon.pencolor(random_color())
#     # kleon.color(random_color())
#     kleon.forward(30)
#     kleon.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

