class car:
	""""This is a class that represents a car"""
	def __init__(self, make, model,year):
		self.make = make
		self.model = model
		self.year = year
		self.omometer_read = 0

	def	describle_car(self):
		d = (f'here is a {self.make}, {self.model} {self.year} with '
			 f'{self.omometer_read} miles on the clock, isnt she a beaut?')
		return d

	def read_omometer(self):
		return print(f'the miles done are: {self.omometer_read}')

	def update_omometer(self, x):

		if x <= self.omometer_read:
			return print('we are not update the miles sorry invalid number')
		else:
			self.omometer_read = x
		return print(f'there has been an update on the miles: {self.omometer_read}')

	def incoroment_omometer(self):
		self.omometer_read += 1
		return print(f'miles going up by 1 {self.omometer_read}')

class EletricCar(car):

	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery_size = battery()



class battery():
	def __init__(self):
		self.battery_size = 45

	def battery_size_des(self):
		d = f'the battery size of this car is: {self.battery_size} KWH'
		return d

	def get_range(self):
		if self.battery_size == 45:
			return print('you get 150 miles')
		elif self.battery_size == 65:
			return print('you get 450 miles')

	def change_battery(self, x):
		if x == 45:
			return print(f'{x} is standard, you canot upgrade this')
		elif x == 65:
			self.battery_size = 65
			return print(f'you have upgraded form 45 to {x}')

		return print('invalid number')