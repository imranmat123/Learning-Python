from ice_cream import IceCreamStand
from admin import Admin
from die import die as d
from random import randint

ice = IceCreamStand('ice scream', 'ice creame')
a = Admin('imran','matloob', 20,'lol','M')
dice = d()

print(a.priv.check_your_privaledge())

lotto = (1,3,5,7,9, 'a', 'f', 'h', 'k', 'y')

for i in range(10):
	print(dice.random())
	i = i + 1

for i in range(20):
	print(dice.twentyDieRan())


lottoList = []

for i in range(10):
	lottoList.append(lotto[randint(0, len(lotto) -1)])

print(lottoList)

my_ticket = []
count = 0
flag = True

while flag:
	for i in range(10):
		my_ticket.append(lotto[randint(0, len(lotto) - 1)])

	if count == 100:
		my_ticket = [1,2,3,4,5,6,7]
		lottoList = [1,2,3,4,5,6,7]

	if len(my_ticket) != len(lottoList):
		print('lenths can be differnt')
	if my_ticket == lottoList:
		flag = False
	else:
		count = count + 1
		print(count)
		my_ticket = []



print(f'it took you {i} times to win the lotto')
print(f'winning ticket is: {my_ticket}')
print(f'lotto ticket is: {lottoList}')




