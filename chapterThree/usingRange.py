for oneToTwenty in range(1,21):
    print(oneToTwenty)

oneMillion = []

for value in range(1,1_000_001):
    oneMillion.append(value)

print(oneMillion)

print(max(oneMillion))
print(min(oneMillion))
print(sum(oneMillion))

for oddNumbers in range(1,21,2):
    print(oddNumbers)

threes = []

for value in range(3,31,3):
    threes.append(value)

print(threes)

cubes = []

for value in range(1, 10):
    c = value**3
    cubes.append(value**3)

print(cubes)

tenCubes = [value**3 for value in range(1,10)]

print(tenCubes)