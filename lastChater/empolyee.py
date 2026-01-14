class empolyee:
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_salary(self):
		return self.salary

	def give_rise(self, amount = 0):
		if amount:
			a = self.salary + amount
			self.salary = a
			return a
		else:
			a = self.salary + 5000
			self.salary = a
			return a
