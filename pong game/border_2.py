from turtle import Turtle

class Border(Turtle):
	def __init__(self):
		super().__init__()

		self.color("black")
		self.shape("square")
		self.turtlesize(stretch_wid=1, stretch_len=3, outline=None)
		self.left(90)
		self.penup()
		self.goto(-320,0)
	def up(self):
		if self.ycor() <240:

			self.fd(40)

	def down(self):
		if self.ycor() > -240:
			self.fd(-40)



