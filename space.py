import turtle

rocket=turtle.Turtle()
space=turtle.Screen()
spaceman=turtle.Turtle()
spaceman.penup()
spaceman.goto(-103,255)
space.addshape("208643_b4fed8b63b6f6bf5cf88.gif")
spaceman.shape("208643_b4fed8b63b6f6bf5cf88.gif")

space.bgpic("172334_eaf0164151f02f6db0a5.gif")

space.addshape("202279_82d5bf3e097847fa453b.gif")
space.addshape("rocketdown.gif")
space.addshape("rocketleft.gif")
space.addshape("rocketright.gif")

rocket.shape("202279_82d5bf3e097847fa453b.gif")
rocket.penup()
rocket.goto(180,-250)
rocket.speed(1000)

def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape("202279_82d5bf3e097847fa453b.gif")
def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape("rocketdown.gif")
def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape("rocketleft.gif")
def right():
    rocket.forward(10)
    rocket.shape("rocketright.gif")


turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()

while True:
    space.update()
    if rocket.distance(spaceman) < 10:
        space.bgpic("511926_657cc317c0f7abd59f22.gif")



turtle.done()
