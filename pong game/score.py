from turtle import Turtle

class Score_1(Turtle):
	def __init__(self,score1=0):
		super().__init__()
		self.color("black")
		self.up()
		self.goto(-180,260)
		self.score1 = score1
		self.write(f"Score = {self.score1} ", False, align="center",font=('Arial',15,'bold'))
		self.ht()




class Score_2(Turtle):

	def __init__(self,score2):

		super().__init__()
		self.color("black")
		self.up()
		self.goto(180,260)
		self.score2 = score2
		self.write(f"Score = {self.score2} ", False, align="center",font=('Arial',15,"bold"))
		self.ht()



