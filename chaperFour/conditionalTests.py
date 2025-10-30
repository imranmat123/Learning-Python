cars = ["bmw", "audi", "subaru", "toyota"]
cars.sort()
for v in cars:
	if v == "bmw":
		print(v.upper())
	else:
		print(v.title())

car = "HoNdA"
print(car.lower() == "honda")


pizzaTopping = ["mUsHrOOomS", "SIlArMi" "pEpPeRoNi", "piNEaPPle"]

for topping in pizzaTopping:
	if topping.lower() != "pineapple":
		print("thank fucking god")
	else:
		print("you are on sick mofo")

#value of the list is 30
listOne = [5,10,15]

#value of the list is 29
listTwo = [29]

if sum(listOne) == 30 and sum(listTwo) == 30:
	print("hey, youre old man ")
else:
	print("no dice")

listTwo.append(1)

if sum(listOne) == 30 and sum(listTwo) == 30:
	print("hey, youre old man ")
else:
	print("no dice")


age0 = 21
age1 = 18

print(age0 >= 22)
print(age1 >= 22)

if age0 >= 22 or age1 >= 22:
	print("you can drink?!")
else:
	print("unlukcy")

if age0 >= 18 or age1 >= 18:
	print("you can dirnk in the uk tho!")
else:
	print("unlucky")


names = ["imran", "ellie", "bhuna", "basil"]

print("bhuna" in names)

for name in names:
	if name.lower() == "bhuna":
		print("best cat in the world")
	else:
		print("worst cats in the world")


users = ["jimmy", "ramon", "andrew", "miguel"]

bannedUsers = ["miguel"]

for u in users:
	if u not in bannedUsers:
		print(f"welcome, {u.title()}")
	else:
		print(f"da fuck you want? dip-shit {u.title()}")


#create at least 10 tests:

#test 1

five = 5
six = 6

if five < six:
	print(f"i think this true will be true, as five is less than 6:"
		  f" {five < six}"
		  )

#test 2
name = "imran"
nameTwo = "IMRAN"

if name.lower() == nameTwo.lower():
	print(f"I think this will be true, as i am using the lower() methord,"
		  f"comparing lowercase to each other "
		  f"{name.lower() == nameTwo.lower()}"
		  )

#test 3
age1 = 30
age2 = 25

if age1 == 30 or age2 == 20:
	print(f"we are using the 'or' keyword, thus this will be true as one of our "
		  f"conditionals have been met: {age1 ==30}, or {age2 == 20}")

#test 4
if age1 < 45 and age2 > 20:
	print(f"this conditional will be true and both conditionals are true:"
		  f"{age1 < 45} and {age2 > 20}")

#test 5
print("\n test 5")
lsitOfNames = ["one", "two", "three", "four"]

if 'one' in lsitOfNames:
	print(f"i think this will be true as one is in the list of names:"
		  f"{'one' in lsitOfNames}"
		  )

#test 6
print("\n test 6")
notInList = ["four"]
for u in lsitOfNames:
	print(u)
	if u not in notInList:
		print(f"this will evaluate to true, as the user is not in this 'notInList'")
	else:
		print(f"this will evaluate to false, as i put four(the user) in the notInList"
			  f" {u not in notInList}")

print("\ntest 7")
#test 7
clearListOfUsers = ["imran", "ellie", "bhuna", "basil", "excuse me?"]
bannedList = ["excuse me?"]

if clearListOfUsers[4] not in bannedList:
	print("you wont see this")
else:
	print(f"this may return false, and the last index is in the bannedList "
		  f"{clearListOfUsers[4] not in bannedList}"
		  )

#test 8
print("\n test 8")
numbers = [1,2,3,4,5,6, 10]
notInNumbers = [10]

for n in numbers:
	if n not in notInNumbers:
		print(f"this will evaluate to true, for the first 6 indexes:"
			  f" {n not in notInNumbers}"
			  )
	else:
		print(f"on the 7th index, we should get a false: {n not in notInNumbers}"
			  f" maybe an off by one error too lol")

#test 9
number = 7
number2 = 8
if number + number2 != 15:
	print("it does equal 15")
else:
	print("it doesnt lol")

#test 10

number = 7
number2 = 8

if number + number2 < 15:
	print("you wont see this")
else:
	print("you will see this tho")
