#boring python graphical import turtle
import turtle

pen = turtle.Turtle()
turtle.title("A gift made in airport, To Petra:")

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    pen.hideturtle()

    # function for creation of eye
def eye(col, rad):
	pen.down()
	pen.fillcolor(col)
	pen.begin_fill()
	pen.circle(rad)
	pen.end_fill()
	pen.up()

def smile():
    # draw face
    pen.width(4)
    pen.fillcolor('yellow')
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    pen.up()

    

    # draw eyes
    pen.goto(-40, 120)
    eye('white', 15)
    pen.goto(-37, 130)
    eye('black', 5)
    pen.goto(40, 120)
    eye('white', 15)
    pen.goto(37, 130)
    eye('black', 5)

    # draw mouth
    pen.goto(-40, 85)
    pen.down()
    pen.right(90)
    pen.circle(40, 180)
    pen.up()

    # draw tongue
    pen.goto(-10, 45)
    pen.down()
    pen.right(180)
    pen.fillcolor('red')
    pen.begin_fill()
    pen.circle(10, 180)
    pen.end_fill()
    pen.hideturtle()

userInput = input("Are u Petra? Yes/No ")
if userInput == "Yes":
    heart()
else:
    smile()

turtle.done()