class car:
	def __init__(self, make, model,year):
		self.make = make
		self.model = model
		self.year = year

	def	describle_car(self):
		d = f'here is a {self.make}, {self.model} {self.year} isnt she a beaut?'
		return d

class EletricCar(car):

	def __init__(self, make, model, year, battery_size):
		super().__init__(make, model, year)
		self.battery_size = battery_size

	def battery_size_des(self):
		d = f'the battery size of this car is: {self.battery_size} KWH'
		return d