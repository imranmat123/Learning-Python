endLoop = ""
GuessTheCountry = ""
country = "england"
while endLoop != "Q":
    GuessTheCountry = input("Please Guess the Country")
    if country == GuessTheCountry:
        print("well done you have won!")
        endLoop = input("do you want to try again? Press Q to quit, or anything else to play again")
    else:
        print("try again")

print("Thank you for playing")