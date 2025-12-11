from random import randint
class die:

	def __init__(self, sides=6):
		self.side = sides

	def random(self):
		return randint(0,self.side)

	def twentyDieRan(self):
		a = self.side = 20
		return  randint(0, a)