import turtle

ground=turtle.Screen()
ground.bgpic("bg1.png")
ground.addshape("left1.gif")
ground.addshape("right1.gif")
ground.addshape("ball.gif")

rightplayer=turtle.Turtle()
rightplayer.penup()
rightplayer.shape("right1.gif")
rightplayer.goto(400,-200)

leftplayer=turtle.Turtle()
leftplayer.penup()
leftplayer.shape("left1.gif")
leftplayer.goto(-400,200)

ball=turtle.Turtle()
ball.penup()
ball.shape("ball.gif")

rightpen=turtle.Turtle()
rightpen.penup()
rightpen.hideturtle()
rightpen.goto(100,250)
rightpen.color("white")
rightpen.write("Rightplayer score: 0",font=("times new roman",27,"bold"))

leftpen=turtle.Turtle()
leftpen.penup()
leftpen.hideturtle()
leftpen.goto(-400,250)
leftpen.color("white")
leftpen.write("Leftplayer score: 0",font=("times new roman",27,"bold"))

def leftplayerup():
    y=leftplayer.ycor()
    leftplayer.sety(y+10)

def leftplayerdown():
    y=leftplayer.ycor()
    leftplayer.sety(y-10)

def leftplayerright():
    x=leftplayer.xcor()
    leftplayer.setx(x+10)

def leftplayerleft():
    x=leftplayer.xcor()
    leftplayer.setx(x-10)

def rightplayerup():
    y=rightplayer.ycor()
    rightplayer.sety(y+10)

def rightplayerdown():
    y=rightplayer.ycor()
    rightplayer.sety(y-10)

def rightplayerright():
    x=rightplayer.xcor()
    rightplayer.setx(x+10)

def rightplayerleft():
    x=rightplayer.xcor()
    rightplayer.setx(x-10)

turtle.onkeypress(leftplayerup,"w")
turtle.onkeypress(leftplayerdown,"s")
turtle.onkeypress(leftplayerright,"d")
turtle.onkeypress(leftplayerleft,"a")
turtle.onkeypress(rightplayerup,"Up")
turtle.onkeypress(rightplayerdown,"Down")
turtle.onkeypress(rightplayerright,"Right")
turtle.onkeypress(rightplayerleft,"Left")

turtle.listen()
dx=5
dy=1
leftscore=0
rightscore=0
while True:
    ball.speed(5)
    x=ball.xcor()
    y=ball.ycor()
    ball.setpos(x+dx,y-dy)

    if rightplayer.distance(ball)<50:
        dx=-dx
        dy=-dy
        
    
    if leftplayer.distance(ball)<50:
        dx=-dx
        dy=dy

    if ball.ycor()<-280:
        dy=-dy

    if ball.ycor()>280:
        dy=-dy

    if ball.xcor()<-450:
        ball.goto(0,0)
        rightpen.clear()
        rightscore=rightscore+1
        rightpen.write("Rightplayer score: {}".format(rightscore),font=("times new roman",27,"bold"))

    if ball.xcor()>450:
        ball.goto(0,0)
        leftpen.clear()
        leftscore=leftscore+1
        leftpen.write("Leftplayer score: {}".format(leftscore),font=("times new roman",27,"bold"))

    
        
turtle.done()