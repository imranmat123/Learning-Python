def place_of_city(city, country, population=''):
	"""function at neatly outputs a formatted string about a country and city"""
	if population:
		a = (f'The city: {city}, is location in {country} and the population is:'
		 f' {population}')
	else:
		a = f'The city: {city}, is location in {country}'
	return a
