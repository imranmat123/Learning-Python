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


class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavours = ['strawberry', 'banana', 'chocolate']



	def describle_flavour(self):
		print(f'the ice cream flavours we currently have are: {self.flavours}')
		u = input('would you like one?')

		if u.lower() == 'yes':
			print(self.flavours)
			u = input('what flavour would you like?')
			for i in self.flavours:
				if i == u:
					return self.pick_flavour(u)

			return print('we dont have that one sorry')
		else:
			return print('ok nps')

	def pick_flavour(self, flavour):
		i = f'here is your flavor {flavour}'
		return print(i)

