myFood = ["pizza","potatoes", "pie", "pasta", "bread", "sauce", "meat", "bacon", "sausage"]

for value in myFood[:3]:
    print(f"the first 3 items in a list are: {value.title()}")
print("\n")
for value in myFood[3:-3]:
    print(f"the middle 3 items in a list are: {value.title()}")
print("\n")
for value in myFood[-3:]:
    print(f"the last 3 items in a list are: {value.title()}")


print(myFood[:3])
print(myFood[3:-3])
print(myFood[-3:])

#more loops i guess:

for value in myFood:
    print(value)

for value in myFood[:3]:
    print(value)
for value in myFood[3:-3]:
    print(value)
for value in myFood[-3:]:
    print(value)