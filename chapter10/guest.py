from pathlib import Path

p = Path('guest')

flag = True
names = ''
while flag:
	name = input('whats your name?')
	if name != 'q':
		names = names + name + '\n'
	else:
		flag = False

p.write_text(names)