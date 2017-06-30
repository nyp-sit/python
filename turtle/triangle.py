import turtle

window = turtle.Screen()

turtle.speed(0)
for i in range(1000) :
    for s in range(3) :
        turtle.forward(i)
        turtle.left(120)
    turtle.left(5)


turtle.exitonclick()
