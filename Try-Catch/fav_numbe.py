import json
from pathlib import	Path

fav_number = Path('fav_number,json')
add = input('do you want to add to the file? Type "y" or "no"')


def welcome_user(userName):
	print(userName)
	return print(f'welcome back {userName}')

def create_user(name, age, fNumber):
	user = {'name': name, 'age': age, 'fav_numbber': fNumber}
	content = json.dumps(user)
	fav_number.write_text(content)
	f = fav_number.read_text()
	content = json.loads(f)
	l = content['name']
	welcome_user(l)

if add.lower() == 'no':
	if fav_number.exists():
		f = fav_number.read_text()
		content = json.loads(f)
		print(f'{content}')
	else:
		print('but you dont have a number?')
else:
	f = fav_number.read_text()
	content = json.loads(f)
	r = input(f'is this your user name? {content['name']}?')

	if r.lower() == 'y':
		welcome_user(str(content['name']))
	else:
		name = input('what is your name?')
		age = input('how old are you')
		fNumber = int(input('What is your fav number?'))
		create_user(name,age,fNumber)



