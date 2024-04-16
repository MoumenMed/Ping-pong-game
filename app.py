import turtle

wind = turtle.Screen()
wind.title("ping pong by moumen")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

#1
bar1 = turtle.Turtle()
bar1.speed(0)
bar1.shape("square")
bar1.color("red")
bar1.penup()
bar1.goto(-360, 0)
bar1.shapesize(stretch_wid=5, stretch_len=1)

#2
bar2 = turtle.Turtle()
bar2.speed(0)
bar2.shape("square")
bar2.color("blue")
bar2.penup()
bar2.goto(360, 0)
bar2.shapesize(stretch_wid=5, stretch_len=1)

#3
balon = turtle.Turtle()
balon.speed(0)
balon.shape("circle")
balon.color("white")
balon.penup()
balon.goto(0, 0)
balon.dx = 1
balon.dy = 1

#functions
def bar1_up():
    y = bar1.ycor()
    y += 20
    bar1.sety(y)   
def bar1_down():
    y = bar1.ycor()
    y -= 20
    bar1.sety(y)

wind.listen()
wind.onkeypress(bar1_up, "z") 
wind.onkeypress(bar1_down, "s")


def bar2_up():
    y = bar2.ycor()
    y += 20
    bar2.sety(y)
def bar2_down():
    y = bar2.ycor()
    y -= 20
    bar2.sety(y)
wind.onkeypress(bar2_up, "Up") 
wind.onkeypress(bar2_down, "Down")

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("courier",24,"normal"))
while True:
    wind.update()
    balon.setx(balon.xcor() + balon.dx)
    balon.sety(balon.ycor() + balon.dy)
    if balon.ycor() >290:
        balon.sety(290)
        balon.dy *= -1

    if balon.ycor() <-290:
        balon.sety(-290)
        balon.dy *= -1

    if balon.xcor() >390:
        balon.goto(0, 0)
        balon.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("courier",24,"normal"))

    if balon.xcor() <-390:
        balon.goto(0, 0)
        balon.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("courier",24,"normal"))

    #fach kitla9a lbalon m3a lbar
    if (balon.xcor() > 340 and balon.xcor() < 350) and (balon.ycor() < bar2.ycor() + 40 and balon.ycor() > bar2.ycor() -40):
        balon.setx(340)
        balon.dx *= -1

    if (balon.xcor() < -340 and balon.xcor() > -350) and (balon.ycor() < bar1.ycor() + 40 and balon.ycor() > bar1.ycor() -40):
        balon.setx(-340)
        balon.dx *= -1
