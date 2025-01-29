import turtle
import random

segment=[]
grass=turtle.Screen()
grass.bgpic("bg2.gif")
grass.addshape("headup.gif")
grass.addshape("headdown.gif")
grass.addshape("headright.gif")
grass.addshape("headleft.gif")
grass.addshape("body.gif")
grass.addshape("gameover.gif")

snake=turtle.Turtle()
snake.penup()
snake.speed(0)
snake.goto(0,0)
snake.setheading(90)
snake.shape("headup.gif")

food=turtle.Turtle()
food.penup()
food.speed(500)
food.color("red")
food.shape("circle")
food.goto(20,50)

pen=turtle.Turtle()
pen.penup()
pen.speed(500)
pen.hideturtle()
pen.goto(0,250)
pen.write("SCORE: 0",font=("times new roman",27,"bold"))


def move():
    snake.forward(10)

def up():
    if snake.heading()!=270:
        snake.setheading(90)
        snake.shape("headup.gif")
def down():
    if snake.heading()!=90:
        snake.setheading(270)
        snake.shape("headdown.gif")
def right():
    if snake.heading()!=180:
        snake.setheading(0)
        snake.shape("headright.gif")
def left():
    if snake.heading()!=0:
        snake.setheading(180)
        snake.shape("headleft.gif")

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()
score=0
while True:
    grass.update()

    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        grass.bgpic("gameover.gif")
        food.hideturtle()

    for i in segment:
        if i.distance(snake)<1:
            grass.bgpic("gameover.gif")
            food.hideturtle()

    if snake.distance(food) < 15:
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        food.setpos(x,y)
        score=score+1
        pen.clear()
        pen.write("SCORE: {}".format(score),font=("times new roman",27,"bold"))
        body=turtle.Turtle()
        body.penup()
        body.shape("body.gif")
        body.speed(0)
        segment.append(body)
    for i in range(len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y=segment[i-1].ycor()
        segment[i].goto(x,y)

    if len(segment)>0:
        x=snake.xcor()
        y=snake.ycor()
        segment[0].goto(x,y)
    move()


turtle.done()
