from turtle import Turtle,Screen
from border_2 import *
from score import *
from border_3 import *
from ball import *
import time
screen_on = Screen()
screen_on.title("Pong Game")
screen_on.tracer(0)
tur2 = Border()
tur3 = center_Border()
score1 = 0
score2 = 0
score_board_1 = Score_1(score1)
score_board_2 = Score_2(score2)
b = Ball()
tur = Turtle()
tur.shape("square")
tur.turtlesize(stretch_wid=1, stretch_len=3, outline=None)
tur.left(90)
tur.color("black")
tur.up()
tur.goto(320,0)
def up():
	if tur.ycor() <240:
		tur.fd(40)
def down():
	if tur.ycor() > -240:
		tur.fd(-40)
screen_on.onkey(up, "Up")
screen_on.listen()
screen_on.onkey(tur2.up, "w")
screen_on.listen()
screen_on.onkey(down, "Down")
screen_on.listen()
screen_on.onkey(tur2.down,"s")
screen_on.listen()
game_on = True
while game_on:
	screen_on.update()
	b.move()
	if b.ycor()>270 or b.ycor() < -270:
		b.bounce()
	elif b.distance(tur)<29:
		b.bounce_from_border()
		# score2 +=1
		# score_board_2.clear()
		# score_board_2 = Score_2(score2)
	elif b.distance(tur2)<29:
		b.bounce_from_border()
		# score1 +=1
		# score_board_1.clear()
		# score_board_1 = Score_1(score1)
	elif b.xcor()>350 :
		b = Ball()
		score1 +=1
		score_board_1.clear()
		score_board_1 = Score_1(score1)
	elif b.xcor() <-350:
		b= Ball()
		score2 +=1
		score_board_2.clear()
		score_board_2 = Score_2(score2)
	time.sleep(0.050)
screen_on.exitonclick()