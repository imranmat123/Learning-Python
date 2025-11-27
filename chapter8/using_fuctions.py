from fun_with_functions import greet_users
import fun_with_functions
from fun_with_functions import fav_book as fb
from fun_with_functions import display_message as dm
from fun_with_functions import	make_album as ma
from fun_with_functions import fact


namess = ['imran', 'ellie', 'basil']

greet_users(namess)



unprinted_designes = ['phone case', 'cup', 'table']
complated_designes = []

fun_with_functions.complatedddd_designs(unprinted_designes, complated_designes)
fun_with_functions.print_complated_design(complated_designes)


paris = fun_with_functions.city_country('paris', 'france')

roma = fun_with_functions.city_country(name_of_city='roma', country='italy')

london = fun_with_functions.city_country(country='england', name_of_city='london')

print(f"{paris}, || {london}, || {roma}")


fun_with_functions.define_pet(pet_type = "cat", pet_name = "basil", )
fun_with_functions.define_pet("Bhuna", "cat")

fb("harry potter")

dm()


imran = ma('imran is the best', 'ellie sucks ballz', 25)
ellie= ma(album_title='imran sucks ballz', artist_name='ellie is the best')
basil = ma(artist_name='bhuna is the best', album_title='suck my ballz', number_of_songs='11')


flag = True
while flag:
	print('you can press q to quit at anytime')
	artist_name = input('what is the artists name? ')
	album_title = input('what is the title of the album? ')
	number_of_songs = input('does the albim have songs? ')

	if artist_name == 'q' or album_title == 'q' or number_of_songs == 'q':
		flag = False

	album = ma(artist_name, album_title, number_of_songs)
	print(album)


print(fact(5))


messages = ['imran', 'ellie', 'basil']
sent_message = []

fun_with_functions.send_messages(messages[:], sent_message)

print('--------------')
fun_with_functions.show_messages(messages)
fun_with_functions.show_messages(sent_message)

