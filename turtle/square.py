import turtle

window = turtle.Screen()
myTurtle = turtle.Turtle()
myTurtle.speed(1)

for j in range(6) :

    for i in range(4) :
        myTurtle.forward(100)
        myTurtle.left(90)
    myTurtle.left(60)


myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)


turtle.exitonclick()
