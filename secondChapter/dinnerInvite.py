guest_list = ["hitler", "churchill","starling"]
inviteStatement = "we are inviting you to a fight to the death, your opponents are people you dont like!"
print(f"{guest_list[0].title()}, {inviteStatement}")
print(f"{guest_list[1].title()}, {inviteStatement}")
print(f"{guest_list[2].title()}, {inviteStatement}")

guessed_who_died = guest_list.pop(2)
guest_list.insert(2, "basil")

print(f"Unfortunately, {guessed_who_died.title()} died, so we've invited someone else, {guest_list[2].title()}")
print(f"The people invited are as follows: {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()}, thank you for your time on this matter")


inviteStatement2 = "we are inviting you to a fight to the death, your opponents are people you dont like!"

print(f"\n{guest_list[0].title()}, {inviteStatement2}")
print(f"{guest_list[1].title()}, {inviteStatement2}")
print(f"{guest_list[2].title()}, {inviteStatement2}")

guest_list.insert(1,"ellie")
guest_list.append("imran")
guest_list.insert(0,"bhuna")

print(f"\n{guest_list[0].title()}, {inviteStatement2}")
print(f"{guest_list[1].title()}, {inviteStatement2}")
print(f"{guest_list[2].title()}, {inviteStatement2}")
print(f"{guest_list[3].title()}, {inviteStatement2}")
print(f"{guest_list[4].title()}, {inviteStatement2}")
print(f"{guest_list[5].title()}, {inviteStatement2}")

numberOfPeople = len(guest_list)
print(f"The number of people we are inviting are: {numberOfPeople}")

notEnoughSpace = "Due to space reasons, we have to uninvite you form the party"

basil = guest_list.pop(4).title()
bhuna = guest_list.pop(0).title()


print(f"\n{guest_list.pop(0).title()}, {notEnoughSpace}")
print(f"{guest_list.pop(1).title()}, {notEnoughSpace}")
print(f"{bhuna.title()}, {notEnoughSpace}")
print(f"{basil.title()}, {notEnoughSpace}")

sentRreply = "MEOW!"

print(f"\n {basil.title()} said: {sentRreply}")
print(f" {bhuna.title()} said: {sentRreply}")


actualInv = "you are still invited!"

print(f"{guest_list[0].title()} and {guest_list[1].title()} {actualInv}, its a date?")

del guest_list[0], guest_list[0]

print(guest_list)


alphaUnordered = ["b", "c", "f","r", "q", "a", "h"]


print(sorted(alphaUnordered, reverse=True))

print(alphaUnordered)
alphaUnordered.sort()
print(alphaUnordered)
alphaUnordered.sort(reverse=True)
print(alphaUnordered)

alphaUnordered.reverse()
print(alphaUnordered)
alphaUnordered.reverse()
print(alphaUnordered)