import colorgram
import turtle

# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
#
# # Create a list to hold the colors.
# rgb_colors = []
#
# # Loop through each color and append its RGB value to the list.
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5),
              (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12),
              (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
              (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
              (65, 231, 239), (217, 88, 51)]

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")

t.color("white")
t.penup()
t.goto(-300, -300)
t.pendown()
color_list = [(r/255, g/255, b/255) for r, g, b in color_list]
t.speed(0)

for i in range(1, 101):
    t.fillcolor(color_list[i % len(color_list)])
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    t.penup()
    t.forward(100)
    t.pendown()
    if i % 10 == 0:
        t.setx(-600)
        t.sety(t.ycor() + 100)
        t.setx(-300)

