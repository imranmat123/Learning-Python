friends = ["dylan", "jonny", "jay", "many many more... yes"]

print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())

message = f"well look who it is: {friends[0]}"
message1 = f"well look who it is: {friends[1]}"
message2 = f"well look who it is: {friends[2]}"
message3 = f"well look who it is: {friends[3]}"

print(message)
print(message1)
print(message2)
print(message3)

carMake = ["Honda", "BMW", "VW", "Ople"]
i = 0

while i < carMake.__len__():
    message = f"I really want a: {carMake[i]}"
    print(message)
    i = i +1

