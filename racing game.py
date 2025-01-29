import turtle

road=turtle.Screen()
road.addshape("891720_5666ed237f9176b5c1bd.gif")
road.addshape("882208_8f5b70c9e59a450326c4.gif")
road.bgpic("901171_0c0dfd4b26419f62512f.gif")

redcar=turtle.Turtle()
redcar.setheading(90)
redcar.shape("891720_5666ed237f9176b5c1bd.gif")
redcar.penup()
redcar.goto(-100,-240)

bluecar=turtle.Turtle()
bluecar.setheading(90)
bluecar.shape("882208_8f5b70c9e59a450326c4.gif")
bluecar.penup()
bluecar.goto(100,-240)

def player1():
    redcar.forward(5)
def player2():
    bluecar.forward(5)

turtle.onkeypress(player1,"Up")
turtle.onkeypress(player2,"w")
turtle.listen()
while True:
    road.update()
    if redcar.pos()>=(-100,200):
        road.bgpic("845969_78a7cbf2af069c7f0762.gif")
        bluecar.hideturtle()
    if bluecar.pos()>=(100,200):
        road.bgpic("815134_2c77319320205ba98568.gif")
        redcar.hideturtle()


turtle.done()