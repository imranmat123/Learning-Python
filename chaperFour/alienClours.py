alienColor = 'red'

if alienColor == 'green':
	print("you have just earned 5 points")

if alienColor == 'red':
	print("you have just earned 5 points")
print("\nElse block here:")
if alienColor == 'green':
	print("you have just earned 5 points")
else:
	print("you have just earned 10 points")

print("\nIf block here:")
if alienColor == 'red':
	print("you have just earned 5 points")
else:
	print("you've just earned 10 points")

print("\nIf-elif-else chain block here:")

if alienColor == 'green':
	print("you've just earned 5 points")
elif alienColor == 'yellow':
	print("you've just earned 10 points")
else:
	print("you've just earned 15 points")


print("\nIf-elif-else chain block here: 2")

alienColor = 'yellow'

if alienColor == 'green':
	print("you've just earned 5 points")
elif alienColor == 'yellow':
	print("you've just earned 10 points")
else:
	print("you've just earned 15 points")

print("\nIf-elif-else chain block here: 3")

alienColor = 'green'

if alienColor == 'green':
	print("you've just earned 5 points")
elif alienColor == 'yellow':
	print("you've just earned 10 points")
else:
	print("you've just earned 15 points")


print("\nHow old are you?")
age = 65

if age < 2:
	print("baby")
elif age < 4:
	print("toddler")
elif age < 13:
	print("kid")
elif age < 20:
	print("teenager")
elif age < 65:
	print("adult")
else:
	print("elder")

print("\nLike fruit?")

favFurits = ["apples", "bananas", "figs"]

if 'pares' in favFurits:
	print("you really like pares")
if 'mango' in favFurits:
	print("you really like mango")
if 'apples' in favFurits:
	print("you really like apples")
if 'bananas' in favFurits:
	print("you really like bananas")
if 'figs' in favFurits:
	print("you really like figs")



print("\n")
availble_toppings = ["tomatos", "cheeese", "bacon", "mushrooms"]
requested_toppings = ["tomatos", "bread", "bacon"]

if requested_toppings:
	for at in requested_toppings:
		if at in availble_toppings:
			print(f"adding {at} to your pizza")
		else:
			print(f"we dont have {at.title()} left")
else:
	print("are you sure you want a plain pizza?")