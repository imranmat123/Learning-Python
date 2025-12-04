from car import EletricCar as ec

car =  ec('gold', 'e-sport', 2018)
print(car.describle_car())
car.update_omometer(60_000)
print(car.describle_car())

i = 0

while i < 99:
	i = i + 1
	car.incoroment_omometer()
print(car.describle_car())

