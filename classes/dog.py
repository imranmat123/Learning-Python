class Dog:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def get_age(self):
		return self.age

	def get_name(self):
		return self.name

	def roll_over(self):
		rolling = f'{self.name} is rolling the fuck over'
		return rolling
	def sitting(self):
		sitting = f'now this mofo {self.name} is sitting down'
		return sitting