from restaurant import Restaurant as r

class IceCreamStand(r):

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

