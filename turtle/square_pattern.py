import turtle
for r in range(5, 100, 5) :
    turtle.penup()
    turtle.setpos(-r, -r)
    turtle.pendown()
    for i in range(4) :
        turtle.forward(2*r)
        turtle.left(90)
turtle.exitonclick()


