car = input("What kind of rental car would you like: ")

print(f"let me see if i can find you a {car}")


tables = input("How many are dinning tonight? ")
nTables= int(tables)
if nTables >= 8:
	print(f"appolgies, but since they are {nTables} of you, you'll have to wait")
else:
	print("oh thats very good, please come right this way!")


MO10 = input("put a number in and i'll tell you if its a multiple of 10 ")
nMO10 = int(MO10)

if nMO10 % 10 == 0:
	print(f"the {nMO10} is indeed a multiple of 10")
else:
	print(f"the {nMO10} is not a multiple of 10")
