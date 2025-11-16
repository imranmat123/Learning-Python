
prompt = "hello we are testing a value, please type anything you like,"
prompt += "\n I will repeat it."
prompt += "\n please press type 'quit' to exist "


x = 1

while x < 2:
	print(x)

message = ''
while message != 'quit':
	message = input(prompt)
	if message.lower() != 'quit':
		print(message)
	else:
		message = message.lower()


upToTen = 1

while upToTen < 10:
	upToTen = upToTen + 1
	if upToTen % 2 == 0:
		continue
	else:
		print(upToTen)



user = ''
while user != 'quit':
	user = input("how old are you?")

	if user == 'quit':
		continue

	if int(user) <= 3:
		print(f"your ticket is free since you are {user} years old")
	elif int(user)  <= 12:
		print(f"your ticket is $10 since you are {user} years old")
	elif int(user)  > 12:
		print(f"your ticket is $15 since you are older than 12 years old")



pizzaToppings = []
topping = ''

while topping != 'quit':
	topping = input("what do you want on your pizza? ")
	if topping != 'quit':
		pizzaToppings.append(topping)
		print(f"you've added {topping} to your pizza")
	else:
		print("the pizza toppings are: ",pizzaToppings)


flag = True

while flag:
	age = input("how old are you?")
	iAge = int(age)

	if iAge <= 3:
		flag = False
		print(f"your ticket is free since you are {iAge} years old")
	elif iAge <= 12:
		flag = False
		print(f"your ticket is $10 since you are {iAge} years old")
	elif iAge > 12:
		flag = False
		print(f"your ticket is $15 since you are older than 12 years old")

while True:
	age = input("how old are you?")
	if age == 'quit':
		break

	iAge = int(age)

	if iAge <= 3:
		print(f"your ticket is free since you are {iAge} years old")
	elif iAge <= 12:
		print(f"your ticket is $10 since you are {iAge} years old")
	elif iAge > 12:
		print(f"your ticket is $15 since you are older than 12 years old")


