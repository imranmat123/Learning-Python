import dog as d
import restaurant as r
import users as u
import house as h
import car as c
import animal as a

jack = d.Dog('jack', 7)

print(jack.age)
print(jack.name.title())

restaurant = r.Restaurant('italians are us', 'italian '
											 'food')
restaurant2 = r.Restaurant('bhuna food emporium',
						   'cat food')
restaurant3 = r.Restaurant('basils food emporium',
						   'cat food but italian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())

print(restaurant2.describe_restaurant())
print(restaurant3.describe_restaurant())

imran = u.Users('imran', 'matloob', 27,
				'internet', 'M')
ellie = u.Users('ellie', 'scriciii', 27,
				'internet', 'F')
basil = u.Users('basil', 'matloob', 4,
				'internet', 'M')


print(imran.describe_user())
print(ellie.describe_user())
print(basil.describe_user())

#self, windows, doors, rooms, bathrooms, garden='no'
ttCrowley = h.House(6,7,2,1)
twoB = h.House(10,3,8,2,'yes')
oneCollingWood = h.House(6,2,6,1)

print(ttCrowley.descible_house())
print(twoB.descible_house())
print(oneCollingWood.descible_house())

oneCollingWood.garden = 'yes'

print(oneCollingWood.descible_house())


oneCollingWood.garden = 'no'


oneCollingWood.give_garden('yes')


restaurant.number_served = 23

restaurant.print_serverd()
restaurant.incorment_servered(10)
restaurant.print_serverd()
restaurant.incorment_servered(0)
restaurant.set_number_served(44)
restaurant.print_serverd()

imran.incorment_login_attemps()
imran.incorment_login_attemps()
imran.incorment_login_attemps()
imran.incorment_login_attemps()
imran.incorment_login_attemps()
imran.print_login_attempts()
imran.reset_login_attempts()
imran.print_login_attempts()

ec = c.EletricCar('gold', 'e-sport', 2018)
print(ec.describle_car())


basil = a.cat('white and gray', 'medium', 'male')
print(basil.legs)
print(basil.describle_pet())
print(basil.tail())

iceCream = r.IceCreamStand('ice screem','ice')


iceCream.describle_flavour()

admin = u.Admin('lol1', 'lol2',22,'lol3',
				'M')
admin.privledge.check_your_privaledge()

ec.battery_size.get_range()
ec.battery_size.change_battery(65)
ec.battery_size.get_range()