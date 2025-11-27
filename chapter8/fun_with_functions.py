def display_message():
	print("in this chapter we will be learning "
		  "about functions and how they work")


def fav_book(title):
	print(f"my favorite book is called {title.title()}")



def define_pet(pet_name, pet_type):
	print(f"I have a {pet_type.title()}")
	print(f"My {pet_type.title()} is named {pet_name.title()}")



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





def greet_users(names):

	for name in names:
		msg = f'hello {name.title()}'
		print(msg)



def complatedddd_designs(unprinted_designes,complated_designes):
	while unprinted_designes:
		item = unprinted_designes.pop()
		complated_designes.append(item)

def print_complated_design(complated_designes):
	for design in complated_designes:
		print(f"{design} has just been printed")




def fact(value):
	sum = value
	for number in range(value-1, 0, -1):
		sum = sum * number
	return sum


def show_messages(message):
	if message:
		for i in message:
			print(i)
	else:
		print('empty list ')

def send_messages(message, sent_message):
	while message:
		msg = message.pop()
		print(f"sending {msg} now")
		sent_message.append(msg)
