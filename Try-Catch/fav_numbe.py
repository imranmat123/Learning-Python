import json
from pathlib import	Path

fav_number = Path('fav_number,json')

if fav_number.exists():
	f = fav_number.read_text()
	content = json.loads(f)
	print(f'{content}')
else:
	f = int(input('What is your fav number?'))
	content = json.dumps(f)
	fav_number.write_text(content)
