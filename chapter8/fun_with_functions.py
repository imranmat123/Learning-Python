def display_message():
	print("in this chapter we will be learning "
		  "about functions and how they work")

display_message()

def fav_book(title):
	print(f"my favorite book is called {title.title()}")

fav_book("harry potter")


def define_pet(pet_name, pet_type):
	print(f"I have a {pet_type.title()}")
	print(f"My {pet_type.title()} is named {pet_name.title()}")


define_pet(pet_type = "cat", pet_name = "basil", )
define_pet("Bhuna", "cat")


def build_person(f_name, l_name, age=None):
	person = {'first_name': f_name, 'last_name': l_name}
	if age:
		person['age'] = age
	return person

def city_country(name_of_city, country):
	return f'{name_of_city.title()}, {country.title()}'


def make_album(artist_name, album_title, number_of_songs = None):
	info_album = {'artist': artist_name,'album': album_title}
	if number_of_songs:
		info_album['number of songs'] = number_of_songs
	return info_album



paris = city_country('paris', 'france')

roma = city_country(name_of_city='roma', country='italy')

london = city_country(country='england', name_of_city='london')

print(f"{paris}, || {london}, || {roma}")


imran = make_album('imran is the best', 'ellie sucks ballz', 25)
ellie= make_album(album_title='imran sucks ballz', artist_name='ellie is the best')
basil = make_album(artist_name='bhuna is the best', album_title='suck my ballz', number_of_songs='11')


flag = True
while flag:
	print('you can press q to quit at anytime')
	artist_name = input('what is the artists name? ')
	album_title = input('what is the title of the album? ')
	number_of_songs = input('does the albim have songs? ')

	if artist_name == 'q' or album_title == 'q' or number_of_songs == 'q':
		flag = False

	album = make_album(artist_name, album_title, number_of_songs)
	print(album)
