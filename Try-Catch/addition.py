flag = True
while flag:
	try:
		numOne = int(input("give me your first number"))
		numTwo = int(input("give me your second number"))
	except ValueError:
		print("please give me numbers!!")
	else:
		flag = False
		sum = numOne + numTwo
		print(f'{sum}')

