# import modules
import turtle

# fastest speed
turtle.speed(0)

for i in range(100) :
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(90*i)

turtle.exitonclick()
