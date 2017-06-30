import turtle

num = int(input('Enter number of circles : '))

for i in range(50) :
    for j in range(num) :
        turtle.circle(5*i)
        turtle.left(360/num)
turtle.exitonclick()
