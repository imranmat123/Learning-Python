user_names = ["imran", "ellie", "basil", "bhuna", "admin"]


if user_names:
	for userName in user_names:
		if userName == 'admin':
			print(f"Hellow {userName.title()}, would you like to see the report?")
		else:
			print(f"Hello {userName.title()}")
else:
	print("We need to find some users...")


current_users = ["imran", "ellie", "basil", "bhuna", "admin"]
new_users = ["IMRAN", "andrew","mum", "ElLie"]
case_insenative_users = []

for case in current_users:
	case_insenative_users.append(case.lower())

for user in new_users:
	if user.lower() in case_insenative_users:
		print(f"Sory, you need to your username {user}")
	else:
		print(f"Welcome {user}")


ordinal_numbers = [1,2,3,4,5,6,7,8,9]

for ordinal_number in ordinal_numbers:
	if ordinal_number == 1:
		print(f"{ordinal_number}st")
	elif ordinal_number == 2:
		print(f"{ordinal_number}nd")
	elif ordinal_number < 4:
		print(f"{ordinal_number}rd")
	else:
		print(f"{ordinal_number}th")

