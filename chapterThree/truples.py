resturant = ("eggs", "bacon", "cheese", "chips", "beans")

for v in resturant:
    print(f"the food we have on offer today is: {v.title()}")


# to see if throws error, it did
#resturant[0] = "beans"

#changing the trouple -  it did, as we have reassigned it
resturant = ("green beans", "vegan bacon", "cheese", "chips", "beans")

#re printed the trouple with its newly assigned values
for v in resturant:
    print(f"the food we have on offer today is: {v.title()}")