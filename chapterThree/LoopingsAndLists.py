names = ["imran", "elena", "basil", "bhuna"]
i = 0
for name in names:
    print(name)
    names[i] = name.title()
    print(names[i],"\n")
    i = i + 1

print(name.title())



pizzas = ["margarita", "pepperoni", "all the meats"]

myFriendsPizza = pizzas[:]

pizzas.append("pineapple")
myFriendsPizza.append("ice cream")

for pizza in pizzas:
    print(f"i really like {pizza.title()}")
print("I really love pizza \n")
print(pizzas)


for pizza in myFriendsPizza:
    print(f"i really like: {pizza.title()}")
print("my friend really likes pizza too \n")
print(myFriendsPizza)


felines = ["fishing cat","tiger","cheetah"]

for feline in felines:
    print(f"This feline would make a great pet: {feline.title()}")
print("\nAll these animals are of the feline family, and everyone loves cats righy?!")