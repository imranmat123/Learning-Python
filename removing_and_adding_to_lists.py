from os import remove
from urllib.request import install_opener

#
# unvarifiedUsers = ["imran", "ellie", "basil", "bhuna"]
# varified = []
#
# while unvarifiedUsers:
# 	currentUser = unvarifiedUsers.pop()
# 	print(f"the user {currentUser}")
# 	varified.append(currentUser)
#
# for c in varified:
# 	print(c)
#
#
# teaOrCoffee = {}
#
# active = True
#
# while active:
# 	name = input("what is your name? ")
# 	response = input("do you like tea or coffe? ")
# 	teaOrCoffee[name] = response
# 	flag = input("do you want to continue? (yes/no) ")
#
# 	if flag.lower() == 'no':
# 		active = False
#
# for k,v in teaOrCoffee.items():
# 	print(f"{k.title()} likes {v.title()}")
#
# sandwich_order = ["tune mayo", "cheese", "blt"]
# finished_sandwiches = []
#
# while sandwich_order:
# 	currentSan = sandwich_order.pop()
# 	print(f"I am making a {currentSan}")
# 	finished_sandwiches.append(currentSan)
#
# for i in finished_sandwiches:
# 	print(f"I have made {i.title()}")
#
# sandwich_order = ["pastrami","tune mayo","pastrami", "cheese", "blt", "pastrami"]
# finished_sandwiches = []

# while sandwich_order:
# 	if 'pastrami' in sandwich_order:
# 		print("there is no pastrami")
# 		while 'pastrami' in sandwich_order:
# 			sandwich_order.remove('pastrami')
# 	else:
# 		curr = sandwich_order.pop()
# 		print(f"I am making a {curr} sandwich")
# 		finished_sandwiches.append(curr)
#
# for i in finished_sandwiches:
# 	print(f"I have made {i.title()}")


onePlace = {}
active = True

while active:
	name = input("what is your name? ")
	response = input("if you could go anywhere in the world where would it be? ")
	onePlace[name] = response
	flag = input("do you want to continue? (yes/no) ")
	if flag.lower() == 'no':
		active = False

for k,v in onePlace.items():
	print(f"So {k.title()} would like to go {v.title()}")