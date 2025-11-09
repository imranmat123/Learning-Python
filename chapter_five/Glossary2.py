from chapter_five.dictionaries import fav_language

glossary = {
	"if-statements": "section about how to use if-statements",
	"sets": "about the set() function",
	"dictionaries": "what are dictionaries in python",
	"lists": "what are lists",
	"varibles": "what are varibles",
	"data types": "what are data types",
	"how to use forloops": "using forloops",
	"looping through lists": "how to loop through lists",
	"tuples":"the differance between a truple and a list ",
	"nonesece": "by me",
	"adding": "nothing",
			}

for key, value in glossary.items():
	print(f"glossary key: {key.title()}, \n\t glossary value: {value.title()}")


rivers = {
	"Nile River": "Ethiopia, Eritrea, Sudan, Uganda, Tanzania, Kenya,"
					  " Rwanda, Burundi, Egypt,"
					  " Democratic Republic of the Congo, South Sudan",

	"Amazon River": "Brazil, Peru, Bolivia, Colombia,"
						" Ecuador, Venezuela, and Guyana",

	"Yangtze River": "China",
		}

#river and counties
for river, counties in rivers.items():
	print(f"The {river} run through {counties}")

# river
print("\n")

for river in rivers.keys():
	print(f"the rivers are called: {river.title()}")

#ounties
print("\n")
for counties in rivers.values():
	print(f"the rivers run through {counties} counties")


#taking the poll
fav_language = {
		"imran": "c",
		"ellie": "java",
		"basil": "golang",
		"bhuna": "python",
}

notTakenPoll = ["dylan", "andrew", "jonny"]
poll = list(fav_language.keys()) + notTakenPoll


for k in poll:
	if k in fav_language.keys():
		print(f"Thank you {k.title()} for taking the poll, I really like {fav_language[f"{k}"]} as a language")
	elif k not in fav_language.keys():
		print(f"oi {k} dickhead, take the fucking poll eh")


