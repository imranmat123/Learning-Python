from numbers import Number

alians = []
i = 1
for a in range(30):
	if i % 3 == 0:
		alian = {"color": "green", "difficulty": "low", "points": 1, "number": i}
		alians.append(alian)
	elif i % 5 == 0:
		alian = {"color": "yellow", "difficulty": "high", "points": 15, "number": i}
		alians.append(alian)
	else:
		alian = {"color": "red", "difficulty": "medium", "points": 5, "number": i}
		alians.append(alian)
	i = i + 1

for a in alians[:10]:
	print(a)



fav_lang = {"imran": ["java", "c", "c++"], "ellie": ["go", "rust", "python"],
			"basil": ["c"]}

for k, v in fav_lang.items():
	if len(v) > 1:
		print(f"{k.title()} fav languages are: ")
		for lang in v:
			print("\t",lang.title())
	else:
		print(f"{k} fav language is: {v[0].title()}")


person1 = {"first_name": "imran", "second_name": "lol", "city": "somewhere",
		   "age": 7}
person2 = {"first_name": "ellie", "second_name": "lol2", "city": "somewhere",
		   "age": 9}
person3 = {"first_name": "basil", "second_name": "lol3", "city": "somewhere",
		   "age": 9}

people = [person1, person2, person3]


for p in people:
	full_name = f"{p["first_name"]} {p["second_name"]}"
	location = p["city"]
	age = p["age"]
	print(f"hi {full_name}, i know you live in {location} and you are {age}")

pet1 = {"name":"basil", "owner": "imran", "age": 5}
pet2 = {"name": "bhuna", "owner": "ellie", "age": 4}
pet3 = {"name": "random", "owner":"both", "age": 99}

pets = [pet1, pet2, pet3]

for pet in pets:
	print(f"hello {pet["name"]}, hello owner {pet["owner"]} i know the pet is:"
		  f"{pet["age"]}")

fav_places = {"imran": "italy", "ellie": "grece", "basil": "home"}

for k,v in fav_places.items():
	print(f"hello {k}, i know your fav place is: {v} ")

fav_number = {"imran": [1], "ellie": [4,5,6], "dylan": [7,8,9],
			  "basil": [10,11,12]}
for k,v in fav_number.items():
	if len(v) < 2:
		print(f"{k}\n\t your fav number is {v[0]}")
	else:
		print(f"hello {k}, i fav numbers are:")
		for number in v:
			print(f"\t{number}")


cities = {
	"Tokyo": {
			  "population": 37_000_000,
			  "country":"japan",
			  "fun fact": "During rush hour, the city's extensive train"
						  " networks employ Oshiya, or 'pushers,' to physically"
						  " push people into the crowded train carriages so the"
						  " doors can close. "
			  },
	"Delhi": {
			  "population": 34_000_000,
			  "country": "india",
			  "fun fact": "The National Capital Territory of Delhi has been"
						  " continuously inhabited since at least 600 BC and"
						  " is mentioned in the ancient epic the Mahabharata",

			 },
	"Shanghai": {
 				 "population": 30_000_000,
			     "country": "china",
				 "fun fact": "Train attendants on the high-speed rail link"
							 " between Shanghai and Beijing were reportedly"
							 " trained to smile showing exactly eight teeth,"
							 " a skill that required significant practice. "
				},
	"London": {
				 "population": 9_800_000,
				 "country": "united kingdom",
				 "fun fact": "London's famous black cab drivers must pass a"
							 " rigorous test called 'The Knowledge,' which"
							 " requires them to memorize around 320 popular"
							 " routes, 25,000 streets, and 20,000 landmarks,"
							 " a process that can take up to four years. "
			  },

	"Paris": {
		"population": 11_500_000,
		"country": "france",
		"fun fact": "Despite having over 6,000 streets, Paris famously"
					" has no stop signs for traffic anywhere in the city. "
	},

}

for k,v in cities.items():
	print(f"{k.title()}: ")
	for info, stat in v.items():
		print(type(stat) == int)
		if type(stat) == int:
			i = stat
			print(f"\t{info.title()}: \n\t\t{i}")
		else:
			j = stat
			print(f"\t{info.title()}: \n\t\t{j.title()}")
	print("\n")




