from testing_for_tests import get_formatted_name
print("press 'q' to quit at any time")
while True:
	first = input("what is your first name?")
	if first == 'q':
		break
	last = input("what is your last name?")
	if last == 'q':
		break
	name = get_formatted_name(first, last)
	print(f'\t Neatly formatted name {name}.')