from lastChater.empolyee import empolyee

imran = empolyee('imran', 55, 70_000)

print(imran.salary)
imran.give_rise(2000)
print(imran.salary)
imran.give_rise()
print(imran.salary)