import turtle

turtle.circle(60)
turtle.circle(-90)

turtle.penup()
turtle.sety(75)
turtle.setx(25)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.sety(75)
turtle.setx(-25)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.sety(55)
turtle.setx(0)
turtle.pendown()
turtle.begin_fill()
turtle.forward(20)
turtle.left(120)

turtle.forward(20)
turtle.left(120)

turtle.forward(20)
turtle.left(120)
turtle.end_fill()

turtle.penup()
turtle.home()

turtle.mainloop()