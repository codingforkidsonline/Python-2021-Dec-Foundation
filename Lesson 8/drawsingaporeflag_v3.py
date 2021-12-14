import turtle

# singapore national flag Proportion:	3:2
flag_width = 450
flag_height = 300
radius = 55
star_length = 20

# move the pen to a position so we can draw the flag at the centre of the screen
turtle.penup()
turtle.setpos(-flag_width/2, 0)
turtle.pendown()

# draw a red rectangle filled with red color
turtle.color("red")
turtle.begin_fill()
for i in range(2):
    turtle.forward(flag_width)
    turtle.left(90)
    turtle.forward(flag_height/2)
    turtle.left(90)
turtle.end_fill()   # final direction: point right


# move the pen to the bottom-left corner
turtle.penup()
turtle.right(90)    # direction: point down
turtle.forward(flag_height/2)
turtle.pendown()
turtle.left(90)     # direction: point right

# draw a black border for the flag
turtle.color("black")
for i in range(2):
    turtle.forward(flag_width)
    turtle.left(90)
    turtle.forward(flag_height)
    turtle.left(90) # final direction: point right   




# move the pen to a new postion for drawing a circle
turtle.penup()
current_pos = turtle.pos()
turtle.setpos(current_pos[0]+100, current_pos[1]+170)
turtle.pendown()

# draw the first circle and filled with white color
turtle.color("white")
turtle.begin_fill()
turtle.circle(radius)   # direction: point right
turtle.end_fill()




# move the pen to a new position to draw another circle
turtle.penup()
turtle.forward(20)
turtle.pendown()

# draw the second circle and filled with red color
turtle.color("red")
turtle.begin_fill()
turtle.circle(radius)   # direction: point left
turtle.end_fill()




# move the pen to a new position for drawing the star (bottom-right star)
turtle.penup()
current_pos = turtle.pos()
turtle.setpos(current_pos[0]+10, current_pos[1]+30)
turtle.pendown()

# draw the 5 stars (first one will be the bottom-righ star)
turtle.color("white")
for i in range(1, 6):
    turtle.begin_fill()
    for j in range(5):
        turtle.forward(star_length)
        turtle.right(144)
    turtle.end_fill()

    turtle.penup()
    turtle.left(i*72)
    turtle.forward(35)
    turtle.right(i*72)
    turtle.pendown()

turtle.hideturtle()

