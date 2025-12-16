from pathlib import Path

locaitonOfCats = Path('cats')
locationOfDogs = Path('dogs')
try:

	readingDogs = locationOfDogs.read_text()
except FileNotFoundError:
	pass
else:
	print(readingDogs)
try:
	readingCat = locaitonOfCats.read_text()
except FileNotFoundError:
	pass
else:
	print(readingCat)



