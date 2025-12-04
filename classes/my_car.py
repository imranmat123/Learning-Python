import car as c

car = c.car('VW', 'gold', 2018)

car.describle_car()

print(car.describle_car())
car.update_omometer(60_000)
print(car.describle_car())

i = 0
while i <= 100:
	car.incoroment_omometer()
	i = i + 1

print(car.describle_car())	