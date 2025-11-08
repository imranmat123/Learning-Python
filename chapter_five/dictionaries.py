elena = {'eyes':'brown', 'noise': 'cute', 'hair': 'black' }

print(elena)

elena['fingers'] = 'cold'
elena['smile'] = 'wide'

print(elena)

for k in elena:
	print(elena[k])

alien_0 = {'position-x': 0, 'position-y': 25,'color': 'green', 'points': 5, 'speed': 'medium'}

print(alien_0)

alien_0['color'] = 'red'
print(alien_0['color'])

if alien_0:
	if alien_0['speed'] == 'slow':
		alien_0['position-x'] =+ 1
	elif alien_0['speed'] == 'medium':
		alien_0['position-x'] =+2
	elif alien_0['speed'] == 'fast':
		alien_0['position-x'] =+3
else:
	print("bro its dead!!")

print(alien_0['color'])
print(alien_0['position-x'])

alien_0['speed'] = 'fast'

if alien_0:
	if alien_0['speed'] == 'slow':
		alien_0['position-x'] =+ 1
	elif alien_0['speed'] == 'medium':
		alien_0['position-x'] =+ 2
	elif alien_0['speed'] == 'fast':
		alien_0['position-x'] =+ 3
else:
	print("bro its dead!!")

print(alien_0['color'])
print(alien_0['position-x'])


print(elena)
del elena['hair']
print(elena)
elena['hair'] = 'brown'
print(elena)


fav_language = {
		"imran": "c",
		"ellie": "java",
		"basil": "golang",
		"bhuna": "python",
}

keyNames = list(fav_language.keys())


print(f"{keyNames[0]} fav lanuage is: {fav_language["imran"].title()}")


person = {
	"name":	"ellie",
	"addess": "never you mind",
	"city": "who wants to know?",
	"age": 99,
		}

for p in person:
	print(f"{p.title()}:{person[p]}")


fav_number = {
	"dylan": 27,
	"ellie": 7,
	"mum": 10,
	"imran":1,
			}

print("\n")
print("without loops")
print("\n")
#without loops:
namesOfPeople = list(fav_number.keys())
print(f"{namesOfPeople[0].title()}'s fav number is: {fav_number[f"{namesOfPeople[0]}"]}")
print(f"{namesOfPeople[1].title()}'s fav number is: {fav_number[f"{namesOfPeople[1]}"]}")
print(f"{namesOfPeople[2].title()}'s fav number is: {fav_number[f"{namesOfPeople[2]}"]}")
print(f"{namesOfPeople[3].title()}'s fav number is: {fav_number[f"{namesOfPeople[3]}"]}")


print("\n")
print("loops")
print("\n")
#loop
for n in fav_number:
	print(f"{n.title()}'s fav number is: {fav_number[n]}")

glossary = {
	"list": "what lists are, and how to use them ",
	"print statement": "what is print state are ",
	"conditional tests": "true of false values",
	"if-statements": "if true do this, is false do this",
	"methord": "what a methord is often followd by the . opperator",
	"function": "what a function is",
	"varibles": "how varibles work",
	"data-typrs": "how data types are handled",
}



print("\n")
print("without loops")
print("\n")

gNames = list(glossary.keys())
print(f"{gNames[0].title()}:\n\t {glossary[f"{gNames[0]}"]}")
print(f"{gNames[1].title()}:\n\t {glossary[f"{gNames[1]}"]}")
print(f"{gNames[2].title()}:\n\t {glossary[f"{gNames[2]}"]}")
print(f"{gNames[3].title()}:\n\t {glossary[f"{gNames[3]}"]}")
print(f"{gNames[4].title()}:\n\t {glossary[f"{gNames[4]}"]}")
print(f"{gNames[5].title()}:\n\t {glossary[f"{gNames[5]}"]}")
print(f"{gNames[6].title()}:\n\t {glossary[f"{gNames[6]}"]}")
print(f"{gNames[7].title()}:\n\t {glossary[f"{gNames[7]}"]}")




print("\n")
print("with loops")
print("\n")
for g in glossary:
	print(f"{g.title()}: \n\t P{glossary[g].title()}")


user = {
	"username": "immie",
	"email": "imranm@lol.com",
	"first-name": "imran",
	"last_name": "matloob",
		}

print(user.items())

for k,v in user.items():
	print(f"{k}, {v}")



for key, value in glossary.items():
	print(f"{key}:\n\t {value}")