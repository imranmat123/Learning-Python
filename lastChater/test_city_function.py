from city_function import place_of_city

def test_place_of_city():
	""""testing places of city"""
	places = place_of_city('london', 'uk')
	assert places == 'The city: london, is location in uk'

def test_population_of_place_of_city():
	""""testing population of city"""
	a = place_of_city('london', 'uk', 8_000_000)
	assert a == (f'The city: london, is location in uk and the population is:'
		 f' 8000000')
