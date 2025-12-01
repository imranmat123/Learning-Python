class animal:
	def	__init__(self, legs=4):
		self.legs = legs

	def how_many_legs(self):
		return self.legs
	def tail(self):
		return f'a big bush tail'


class cat(animal):

	def __init__(self, color, size, sex):
		super().__init__()
		self.color = color
		self.size = size
		self.sex = sex

	def describle_pet(self):
		d = (f'The car is {self.color} about {self.size} and is {self.sex}'
			 f'with {self.legs} and {cat.tail(self)}')
