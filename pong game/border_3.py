from turtle import Turtle

class center_Border(Turtle):
	def __init__(self):
		super().__init__()
		self.color("red")
		self.shape("square")
		self.turtlesize(stretch_wid=30, stretch_len=0.090, outline=None)
