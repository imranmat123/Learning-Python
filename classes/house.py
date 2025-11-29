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