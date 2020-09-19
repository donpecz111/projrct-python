import turtle

def kwadrat (bok):
    for p in range(4):
        turtle.forward(bok)
        turtle.left(90)

for x in range(1,4) :
    kwadrat(x*100)


kwadrat(100)
turtle.left(120)
kwadrat(100)
turtle.left(120)
kwadrat(100)
turtle.left(120)


turtle.mainloop()