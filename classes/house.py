class House:

	def __init__(self, windows, doors, rooms, bathrooms, garden='no'):
		self.windows = windows
		self.doors = doors
		self.rooms = rooms
		self.bathrooms = bathrooms
		self.garden = garden


	def descible_house(self):

		if self.garden == 'yes':
			h = (f'this house has {self.windows} windows, {self.doors} doors,'
				 f'{self.rooms} rooms and {self.bathrooms} bathroom.. '
				 f'oh and it has'
				 f'a garden')
		else:
			h = (f'this house has {self.windows} windows, {self.doors} doors,'
			 f'{self.rooms} rooms and {self.bathrooms} bathroom')

		return h

	def give_garden(self, garden):

		if self.garden == 'no' and garden == 'yes':
			g = f'garden has not been updated'
			print('how the fuck did you make a garden out of thing air')

		else:
			g = f'garden has been updated'
			self.garden = garden

		return g

