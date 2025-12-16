from pathlib import Path

book = Path('A_Fishing_Trip_on_the_Planet_Mars')
book1 = Path('Lord_Lister')
book2 = Path('The_Sultanate_of_Bornu_by_Arnold_Schultze')
test = book.read_text(encoding='utf-8')
test1 = book1.read_text(encoding='utf-8')
test2 = book2.read_text(encoding='utf-8')



testCount = test.lower().count('the')
testCount1 = test1.lower().split()
testCount2 = test2.lower().split()


print(len(testCount1))
print(len(testCount2))
print(testCount)
