import turtle




color_list = ["red", "blue", "orange", "purple"]
pensize_list = [2, 4, 6, 10]

for i in range(4):
    line_size = pensize_list[i]
    turtle.pensize(line_size)
    line_color = color_list[i]
    turtle.color(line_color)
    turtle.forward(200)
    turtle.left(90)

