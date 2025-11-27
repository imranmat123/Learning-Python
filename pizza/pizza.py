def sandwitch(bread, *filling):
	return (f"your sandwich will have {bread} bread and the fillings chosen are: "
			f"{filling}")

def user_profile(fName, lName, **kwargs):
	kwargs['first_name'] = fName
	kwargs['second_name'] = lName
	return kwargs

def cars(manu, model, **kwargs):
	kwargs['manufacture'] = manu
	kwargs['model'] = model
	return kwargs

