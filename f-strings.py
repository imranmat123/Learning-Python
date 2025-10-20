fName = "imran"
Sname = "matloob"
age = 50
location = "leeds"

print(f"hello, {fName.title()} {Sname.title()}, I know you live in {location.title()} and you are {age} years old")


message = f"hello, {fName.title()} {Sname.title()}, I know you live in {location.title()} and you are {age} years old"

print(message)


message = f"hi\t my\n name\t is\n {fName}"
print(message)


message = f"{fName}speaks \n\tEnglish\n\tIrish\n\tScottish"
print(message)


stripMessage = " imran "
print(stripMessage.strip())
print(stripMessage.rstrip())
print(stripMessage.lstrip())

removingPrefix = "imran"
removingPrefix = removingPrefix.removeprefix("im")
print(removingPrefix)