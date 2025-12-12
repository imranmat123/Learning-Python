from pathlib import Path

path = Path('pi_million_digits.txt')
learning = Path("what_i've _learnt_in_python_so_far")

print(path.exists())
print(learning.exists())

content = path.read_text().rstrip()
# print(content)
for l in range(len(content.splitlines())):
	print(f'this is line {l} and on this line {content.splitlines()[l]}')

pi_string = ''
for line in content.splitlines():
	pi_string = pi_string + line

print(pi_string[:100])
print(len(pi_string))

birthday = input('is your birthday in pi? enter ddmmyy')

if birthday in  pi_string:
	print("your birthday is in pi")
else:
	print("your birthday is not in pi")

learn = learning.read_text().rstrip()
print(learn)

learningLines = learn.splitlines()

strLean = ''
for l in learn.splitlines():
	strLean = strLean + l
	print(f'{l}')
	print(learningLines)

message = strLean.replace('python', 'c')


print(message)
# learningLines = learn.splitlines()
# for l in learningLines:
# 	print(f'{l}')
# 	print(learningLines)

