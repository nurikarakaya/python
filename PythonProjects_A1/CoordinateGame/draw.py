import turtle

sc = turtle.Screen()

x = turtle.Turtle()
x.hideturtle()
x.penup()
x.setx(-300)
x.showturtle()

y = turtle.Turtle()
y.hideturtle()
y.penup()
y.sety(-300)
y.left(90)
y.showturtle()

x.pendown()
y.pendown()

x.forward(600)
y.forward(600)

coor1 = turtle.Turtle()
coor1.hideturtle()
coor1.penup()
coor1.goto(100, 100)
coor1.shape("circle")
coor1.shapesize(0.5)
coor1.showturtle()
coor1.pendown()
coor1.forward(150)
coor1.left(90)
coor1.forward(150)

coor2 = turtle.Turtle()
coor2.hideturtle()
coor2.penup()
coor2.goto(250, 250)
coor2.shape("circle")
coor2.shapesize(0.5)
coor2.showturtle()
coor2.pendown()
coor2.left(180)
coor2.forward(150)
coor2.left(90)
coor2.forward(150)

turtle.done()
