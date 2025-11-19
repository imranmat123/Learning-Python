def display_message():
	print("in this chapter we will be learning "
		  "about functions and how they work")

display_message()

def fav_book(title):
	print(f"my favorite book is called {title.title()}")

fav_book("harry potter")


def define_pet(pet_name, pet_type):
	print(f"I have a {pet_type.title()}")
	print(f"My {pet_type.title()} is named {pet_name.title()}")


define_pet(pet_type = "cat", pet_name = "basil", )
define_pet("Bhuna", "cat")