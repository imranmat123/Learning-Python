class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		describe_restaurant = (f'the restaurant name is: {self.restaurant_name} '
							   f'and the cuisine is: {self.cuisine_type}')
		return describe_restaurant

	def open_restaurant(self):
		open = f'restaurant is open'
		return open

	def set_number_served(self, number):
		if self.number_served > number:
			print(f'cannot update, incorrect value')
		else:
			self.number_served = number

	def incorment_servered(self,number):
		if number <= 0:
			print('can not update, sorry')
		else:
			self.number_served = self.number_served + number
	def print_serverd(self):
		return print(f'{self.number_served}')


