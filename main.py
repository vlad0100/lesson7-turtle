import turtle

draw = turtle.Turtle()

#for i in range(6):
#    draw.forward(50)
#    draw.right(60)
#num_sides = 6788
#side_length = 2
#angle = 360.0 / num_sides

#for i in range(num_sides):
#    draw.forward(side_length)
 #   draw.right(angle)
#window = turtle.Screen()
#window.bgcolor("gray29")
#window.title("NutuMesterulManolIIII")

#draw.color("white")

#def shapefun(size, sides):
#    for i in range(sides):
#        draw.fd(size)
#        draw.left(360.0 / sides)
#        size = size - 2

#shapefun(150, 4)
#shapefun(140, 4)
#shapefun(130, 4)
#shapefun(120, 4)
#shapefun(110, 4)
#shapefun(100, 4)
#shapefun(90, 4)
#shapefun(80, 4)
#shapefun(70, 4)
#shapefun(60, 4)
#shapefun(50, 4)
#shapefun(40, 4)
#shapefun(30, 4)
#shapefun(20, 4)
#shapefun(10, 4)

window2 = turtle.Screen()
pen = turtle.Pen()
pen.penup()
pen.goto(-220, 50)
pen.pendown()
#colors = ['cyan2', 'yellow1']

def drawM():
    pen.right(75) #Litera V
    pen.forward(40)
    pen.left(150)
    pen.forward(40)
    pen.penup()
    pen.goto(-180, 50) #Litera L
    pen.pendown()
    pen.right(165)
    pen.forward(40)
    pen.left(90)
    pen.forward(20)
    pen.penup()
    pen.goto(-140, 10) #Litera A
    pen.pendown()
    pen.left(70)
    pen.forward(40)
    pen.right(140)
    pen.forward(40)
    pen.penup()
    pen.goto(-134, 25) #Linia de Mijloc la litera A
    pen.pendown()
    pen.left(70)
    pen.forward(17)
    pen.penup()
    pen.goto(-90, 10) #Litera D
    pen.pendown()
    pen.left(90)
    pen.forward(40)
    pen.right(90)
    for i in range(12):
        pen.forward(6)
        pen.right(180/11)
# programul scrie numele VLAD

drawM()
#for i in range(7):
#    pen.pencolor(colors[i%2])
#    pen.width(i/100 + 0.1)
#    pen.forward(i)
#    pen.left(60)
#    pen.speed(1000)

turtle.done()
turtle.exitonclick()